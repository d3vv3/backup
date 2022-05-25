import fcntl
import logging
import os
import shutil
import sys
from pathlib import Path


from movy import checkers

logger = logging.getLogger(__name__)


class Movy:

    lock_file_path = '/tmp/.movy.lock'

    def __init__(self, src, group, dst='./movy'):
        self.src = src
        self.dst = dst
        self.group = group

        if not checkers.check_group(group):
            sys.exit()
        if not checkers.check_folder_exists(src):
            sys.exit()

        self.locked_file_descriptor = self.acquire_lock()

    def acquire_lock(self):
        '''
        Create a lockfile in /tmp and exclusively lock it to avoid
        the program running multiple times
        '''
        locked_file_descriptor = open(self.lock_file_path, 'w+')
        if locked_file_descriptor.writable():
            fcntl.lockf(locked_file_descriptor, fcntl.LOCK_EX)
        return locked_file_descriptor

    def release_lock(self):
        '''
        Release the lockfile in /tmp to allow other process to
        run the program
        '''
        if self.locked_file_descriptor.writable():
            fcntl.lockf(self.locked_file_descriptor, fcntl.LOCK_UN)
        os.remove(self.lock_file_path)

    def backup_item(self, source: str, root_folder: str):
        '''
        Copy a directory or move file from the source path to the
        backup destination
        Args:
            * source (str): path for the original file or directory
            * root_folder (str): full path of the parent folder
        '''
        if checkers.path_owned_by_group(source, self.group):
            relative_path = os.path.relpath(root_folder, self.src)
            new_path = os.path.join(self.dst, relative_path)
            new_file_path = os.path.join(
                new_path, os.path.join(new_path, Path(source).name))
            logger.debug("Moving %s to %s", source, new_path)
            if os.path.isdir(source):
                if not os.path.isdir(new_path):
                    os.makedirs(new_path)
                    self.copy_owner(source, new_path)
            else:
                if not os.path.isdir(new_path):
                    os.makedirs(new_path)
                shutil.move(source, new_file_path)
                path_to_check, _ = os.path.split(source)
                self.delete_dir_if_empty(path_to_check)
        return

    def iterate(self):
        '''
        Iterate through the source directory to backup the files
        '''
        for root, dirs, files in os.walk(self.src):
            for directory in dirs:
                path = os.path.join(root, directory)
                self.backup_item(path, root)
            for filename in files:
                path = os.path.join(root, filename)
                self.backup_item(path, root)

    @staticmethod
    def copy_owner(source: str, new_path: str):
        '''
        Copy the source owner to the target directory.

        Args:
            * source (str): path for the original file or directory
            * new_path (str): path for the target file or directory
        '''
        st = os.stat(source)
        os.chown(new_path, st.st_uid, st.st_gid)

    @staticmethod
    def delete_dir_if_empty(folder: str):
        if not any(os.scandir(folder)):
            os.removedirs(folder)

    def run(self):
        '''
        Move the files
        '''
        if not checkers.check_folder_exists(self.dst, create=True):
            sys.exit()
        logger.info("Moving files from %s to %s for group %s",
                    self.src, self.dst, self.group)
        self.iterate()
        self.release_lock()
        logger.info("Finished")
