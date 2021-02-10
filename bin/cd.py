# EMREX SHELL COMMAND

import os

COMMAND_NAME = "cd"
DESCRIPTION = "Changes Directory"

def command(*args):
    if len(args) != 1:
        return (2, "Wrong argument number.")

    os.chdir(args[0])
    return (4, "")