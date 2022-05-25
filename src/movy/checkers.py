import grp
import os
import logging

logger = logging.getLogger(__name__)


def check_folder_exists(folder_path: str, create: bool = False):
    if os.path.isdir(folder_path) and create is True:
        logger.warning('The folder %s already exists', folder_path)
        overwrite = True if input(
            f"The folder {folder_path} already exists. Overwrite? [Y/n]:"
        ).lower() in ["y", ""] else False
        return overwrite
    if not os.path.isdir(folder_path) and not create:
        logger.error('The folder %s does not exist', folder_path)
        return False
    if not os.path.isdir(folder_path) and create:
        logger.debug('The folder %s does not exist', folder_path)
        logger.debug('Creating %s', folder_path)
        os.mkdir(folder_path)
        return True
    return True


def check_group(group: str):
    '''
    Check if group exists and exit if it doesn't

    Args:
        * group (str): group name
    '''
    try:
        grp.getgrnam(group)
        return True
    except KeyError:
        logger.error('Group %s does not exist', group)
        # sys.exit()
    return False


def path_owned_by_group(file_path: str, group: str):
    stat_info = os.stat(file_path)
    gid = stat_info.st_gid
    return group == grp.getgrgid(gid)[0]
