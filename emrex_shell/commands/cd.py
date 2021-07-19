# EMREX SHELL COMMAND

import os

COMMAND_NAME = "cd"
DESCRIPTION = "Changes Working Directory"


def command(args):
    if len(args) != 1:
        return (1, "Invalid number of arguments.")

    os.chdir(args[0])
    return (3, "")
