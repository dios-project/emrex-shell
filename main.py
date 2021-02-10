"""
Main file of emrex shell.

Error codes:

    1: Successful, with print
    4: Succesful, without print
    2: Argument Error
    3: File/Directory Access error
"""

import os

# TODO: Add config for standard output.

def interpreter(cmd, commands):
    cmd_list = cmd.split()
    command_name = cmd_list[0]
    args = cmd_list[::-1][:-1][::-1] # TODO: Change here. :/

    command_found = False
    for command in commands:
        if command_name == command.COMMAND_NAME:
            result = command.command(*args)
            process_result(result)
            command_found = True
            break
    
    if not command_found:
        print("Command not found.")

def process_result(res):
    error_code, text = res

    if error_code == 1:
        print(text)
    
    elif error_code == 3:
        print("File/Directory Access Error:", text)
    
    elif error_code == 2:
        print("Argument Error:", text)
    
    elif error_code == 4:
        # Don't do anything.
        pass
    
    else:
        print("WARNING: Invalid error code at", res)