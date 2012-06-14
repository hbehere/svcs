from ..repository import Repository

import os
import shutil

def test_create_repository():
    """
    Test to create and initilize repository
    """
    test_repository = Repository("D:\\test_svc")
    storage_path = test_repository.storage_path
    assert storage_path == "D:\\test_svc\\.svcs"
    assert os.path.exists(storage_path)

    # Delete test repository and storage
    shutil.rmtree(storage_path)
