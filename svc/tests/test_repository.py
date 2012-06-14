from ..repository import Repository

import os
import shutil

def test_create_repository(repository_path):
    """
    Test to create and initilize repository
    """
    test_repository = Repository(repository_path)

    storage_path = test_repository.storage_path

    assert storage_path ==  repository_path + os.sep + ".svcs"
    assert os.path.exists(storage_path)
