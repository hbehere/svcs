# This file is command line interface for sample sub version system

from optparse import OptionParser

import os
import sys
import datetime

from ..operations import Repository

def init():
    """
    This create required repository for svc.
    Current working directory would be used as repository path.
    Return repository instance.
    """
    
    return Repository(os.getcwd())
    
def commit(args):
    """
    @param : args - list - list of arguments
    """
    if len(args) < 3:
        print "Insuffciant arguments for commit"
        sys.exit()
        
    if args[0] != '-m':
        print "Incorrect syntax"
        print "Syntax : commit -m <message> <file1> <file2> <file3>"
        
    commit_message = args[1]
    
    files_to_be_commited = args[2:]
    
    r = init()
    
    author = "test@test.org"
    r.commit(msg=commit_message,
             committer=author,
             date=datetime.datetime.now(),
             files=files_to_be_commited)
    
def main():
    """
    Method to handle command line arguments
    """
    pass
    
if __name__=='__main__':
    cl_args = sys.argv
    
    l_cl_args = len(cl_args)
    
    if l_cl_args < 2:
        print "python clip.py command_name [command_arguments]"
        
    command_string = cl_args[1]
    
    if command_string == 'init':
        create_repository()
    elif command_string == 'commit':
        commit(cl_args[2:])
    else:
        print "Incorrect command"