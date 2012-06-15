from ..repository import Repository

import os
import datetime

def test_create_repository(repository_path):
    """
    Test to create and initialize repository
    """
    test_repository = Repository(repository_path)

    storage_path = os.path.join(repository_path,".svcs")

    assert os.path.exists(storage_path)

def test_commit(repository_path):
    """
    Test to commit to repository
    """
    test_repository = Repository(repository_path)
    c_msg = "Sample commit"
    c_commiter = "pytest@test.org"
    current_date = datetime.datetime.now()

    sample_file_path = repository_path + os.sep + "sample.txt"
    sample_file = file(sample_file_path,"ab")
    sample_file.write("This is sample text file")
    sample_file.close()

    # List of files to be commited - list contains path to file
    files_list = [sample_file_path]

    commit_id = test_repository.commit(msg=c_msg,
                                       committer=c_commiter,
                                       date=current_date,
                                       files=files_list)

    commit_path = os.path.join(repository_path, ".svcs", "objects", str(commit_id))

    assert os.path.exists(commit_path)
    
def test_log(repository_path):
    """
    Test to check log for given commit
    """
    
    test_repository = Repository(repository_path)
    test_repository.log()