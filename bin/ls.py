# EMREX SHELL COMMAND

import os

COMMAND_NAME = "ls"
DESCRIPTION = "Classic ls command."

def command(*args):
    if not len(args) <= 1:
        return (2, "Bad arguments.") # 2 means argument error. Second element is error message.
    
    try:
        listdir = os.listdir("." if not args else args[0])
    except FileNotFoundError:
        return (3, "No such file or directory.") # 3 means file/directory access problem.

    result = [1, ""]
    for name in listdir:
        result[1] += name + "\n"
    
    return result