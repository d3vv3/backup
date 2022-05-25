import os
import uuid

from movy import movy


def test_move_lock():
    test_folder = os.path.join('/tmp', str(uuid.uuid4()))
    os.mkdir(test_folder)
    a = movy.Movy(test_folder, os.getlogin())
    assert os.path.exists('/tmp/.movy.lock')
    a.release_lock()
    assert not os.path.exists('/tmp/.movy.lock')
    os.rmdir(test_folder)
