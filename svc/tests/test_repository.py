from ..repository import Repository

import os
import shutil

def test_create_repository():
    """
    Test to create and initilize repository
    """
    repository_path = "D:\\test_svc"
    test_repository = Repository(repository_path)

    storage_path = test_repository.storage_path

    assert storage_path == "D:\\test_svc\\.svcs"
    assert os.path.exists(storage_path)

    # Delete test repository and storage
    shutil.rmtree(repository_path)
