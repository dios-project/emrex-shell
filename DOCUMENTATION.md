# Documentation of emrex Shell

## How this works?

You can think this project as a shell framework. Project reads bin folder (or which folder you want). Each file that it starts with specific prefix is a
command. Prefix:

```python
# EMREX SHELL COMMAND
```

### Standarts of a command file

```python
# EMREX SHELL COMMAND
# File should to start with this prefix.

COMMAND_NAME = "my_command" # Name of command for call
DESCRIPTION = "Foo bar" # Description for help texts.

def command(*args):
    ...
    return (1, "Text") # Example return type. Commands shouldn't print anything.
```

### Return type of command functions

Typically, return values should look like this: 

```python
def command(*args):
    ...
    return (1, "Successful!") # return (status_code, text)
```

Status Code  | Explanation                                                   | Example
------------ | ------------------------------------------------------------- | -----------
1            | Successful. Prints given text.                                | ``return (1, "Successful")``
2            | Some problem about arguments. Prints given text.              | ``return (2, "Too much argument.")``
3            | File directory access error. Prints given text.               | ``return (3, "File not found.")``
4            | Successful. Don't prints any text. Should give a blank string.| ``return (4, "")``
