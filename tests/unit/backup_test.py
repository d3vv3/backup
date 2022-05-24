import os
import uuid

import backup


def test_backup_lock():
    test_folder = os.path.join('/tmp', str(uuid.uuid4()))
    os.mkdir(test_folder)
    a = backup.Backup(test_folder, os.getlogin())
    assert os.path.exists('/tmp/.backup.lock')
    a.release_lock()
    assert not os.path.exists('/tmp/.backup.lock')
    os.rmdir(test_folder)
