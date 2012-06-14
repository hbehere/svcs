# This class handles svc repository

import os

class Repository(object):
    """
    Class for svc reposiotory
    """
    def __init__(self, location):
        """
        Initializes repository.

        Creates .svcs storage directory for given repository path.
        """
        storage_path = location + os.sep + ".svcs"
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)

        self.storage_path = storage_path