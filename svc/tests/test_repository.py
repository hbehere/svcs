from ..repository import Repository

import os
import datetime

def test_create_repository(repository_path):
    """
    Test to create and initilize repository
    """
    test_repository = Repository(repository_path)

    storage_path = test_repository.storage_path

    assert storage_path ==  repository_path + os.sep + ".svcs"
    assert os.path.exists(storage_path)

def test_commit(repository_path):
    """
    Test to commit to repository
    """
    test_repository = Repository(repository_path)
    c_msg = "Sample commit"
    c_commiter = "pytest@test.org"
    current_date = datetime.datetime.now()
    test_repository.commit(msg=c_msg,
                           commiter=c_commiter,
                           date=current_date)