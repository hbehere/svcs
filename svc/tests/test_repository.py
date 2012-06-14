from ..repository import Repository

import os

def test_create_repository():
    """
    Creates and initilizes repository
    """
    test_repository = Repository("D:\\test_svc")
    assert test_repository.storage_path == "D:\\test_svc\\.svcs"
