from ..repository import Repository

import os

def test_create_repository():
    """
    Creates and initilizes repository
    """
    test_repository = Repository()
    assert os.path.exists(test_repository.location)
