import os
import uuid

import checkers


def test_check_group():
    assert checkers.check_group('docker') is True
    assert checkers.check_group(str(uuid.uuid4())) is False


def test_check_folder_exists():
    test_folder = os.path.join("/tmp", str(uuid.uuid4()))
    os.mkdir(test_folder)
    assert checkers.check_folder_exists(test_folder)
    os.rmdir(test_folder)


def test_path_owned_by_group():
    test_folder = os.path.join("/tmp", str(uuid.uuid4()))
    os.mkdir(test_folder)
    os.chown(test_folder, os.getuid(), os.getgid())
    assert checkers.path_owned_by_group(test_folder, os.getlogin())
    os.rmdir(test_folder)
