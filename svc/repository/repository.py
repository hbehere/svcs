# This class handles svc repository

import os

from ..storage import FileStorage, File, Commit

class Repository(object):
    """
    Class for svc reposiotory
    """
    def __init__(self, location):
        """
        @param : location - string - repository path

        Initializes repository.

        Creates .svcs storage directory for given repository path.
        Also Initializes file system storage
        """
        if not os.path.exists(location):
            os.makedirs(location)

        storage_path = location + os.sep + ".svcs"

        self.storage = FileStorage(storage_path)

    def commit(self, msg, committer, date, files):
        """
        @param : msg - string - commit messgae
        @param : committer - string - email of commiter
        @param : date - datetime - date/time detail for commit
        @param : files - list - list of file paths to be commited

        Stores files and creates commit.
        """
        file_ids = []

        # First store file objects
        # We need to get file contains by reading file
        for eachFile in files:
            file_object = open(eachFile,"rb")
            file_contents = file_object.read()
            file_object.close()

            # Store file for svc
            s_file = File(file_contents)
            s_file_id = s_file.id

            # Store file object
            self.storage.store_object(obj=s_file)

            # Update file ids list
            file_ids.append((eachFile, s_file_id))

        # Create commit object
        s_c = Commit(committer=committer,
                     message=msg,
                     date=date,
                     parent=None,
                     files=file_ids,
                     )

        # Store commit as object
        self.storage.store_object(obj=s_c)

        # Update tip with commit
        self.storage.update_tip(commit=s_c)

        # Get commit id
        commit_id = s_c.id

        # Return commit id
        return commit_id
    
    def log(self):
        """
        This method return log for latest commit and all related parent commit
        """
        pass