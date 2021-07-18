# -*- coding:UTF-8 -*-

"""
Core interpreter of emrex Shell.
"""

# TODO: Add config for standard output.


def interpreter(cmd, commands):
    cmd_list = cmd.split()
    command_name = cmd_list[0]
    args = cmd_list[1:]

    command_found = False
    for command in commands:
        if command_name == command.COMMAND_NAME:
            result = command.command(args)
            process_result(result)
            command_found = True
            break

    if not command_found:
        print("Command not found.")


def process_result(res):
    exit_code, text = res

    if exit_code == 0:
        print(text)

    elif exit_code == 1:
        print("Argument Error:", text)

    elif exit_code == 2:
        print("File/Directory Access Error:", text)

    elif exit_code == 3:
        # Don't do anything.
        pass

    else:
        print("WARNING: Invalid exit code at", res)
