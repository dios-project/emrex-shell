# EMREX SHELL COMMAND

import os

COMMAND_NAME = "clear"
DESCRIPTION = "Clears terminal."


def command(args):
    if args:
        return (1, "This command does not takes any argument.")

    os.system("cls" if os.name == "nt" else "clear")
    return (3, "")
