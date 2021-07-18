# EMREX SHELL COMMAND

import os

COMMAND_NAME = "ls"
DESCRIPTION = "Classic ls command."


def command(args):
    if not len(args) <= 1:
        return (1, "Bad arguments.")  # 1 means argument error. Second element is error message.

    try:
        listdir = sorted(os.listdir("." if not args else args[0]))
    except FileNotFoundError:
        return (2, "No such file or directory.")  # 2 means file/directory access problem.

    return (0, "\n".join(listdir))
