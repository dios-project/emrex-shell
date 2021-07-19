#!/usr/env/bin/python3
# -*- coding:UTF-8 -*-

"""
Main file of emrex Shell.
"""

try:
    import core  # For execute with "python -m emrex_shell"
except ImportError:
    from . import core  # For execute with "./emxsh"
import platform
import sys
import os

HOST = platform.node()
USER = os.getlogin()

PATH = ["commands"]
IGNORES = ["__pycache__"]
COMMAND_PREFIX = "# EMREX SHELL COMMAND\n"
PS = "[{user}@{host}: {current_dir}] λ "  # TODO: Make ps more customizable.


COMMANDS = []
for path in PATH:
    path = os.path.join(os.path.dirname(__file__), path)
    sys.path.append(path)

    for item in os.listdir(path):
        if item in IGNORES:
            continue

        with open(os.path.join(path, item), "r") as file:
            if file.readline() == COMMAND_PREFIX:
                module_path = item.rstrip(".py")
                COMMANDS.append(__import__(module_path, fromlist=[""]))

            else:
                print("WARNING: A non command file found in one of the path dirs.")


def main():
    try:
        while True:
            cmd = input(PS.format(user=USER, host=HOST, current_dir=os.getcwd()))
            core.interpreter(cmd, COMMANDS)

    except (KeyboardInterrupt, EOFError):
        print()
        exit(0)  # Change exit code from 1 to 0. Because, 1 exit code mean "exit with minor error".


if __name__ == "__main__":
    main()
