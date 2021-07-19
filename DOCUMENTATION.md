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
DESCRIPTION = "Foo bar"     # Description for help texts.

def command(args):
    ...
    return (0, "Text") # Example return type. Commands shouldn't print anything.
```

### Return type of command functions

Typically, return values should look like this:

```python
def command(args):
    ...
    return (0, "Successful!") # return (exit_code, text)
```

| Exit Code | Explanation                                                    | Example                              |
| --------- | -------------------------------------------------------------- | ------------------------------------ |
| 0         | Successful. Prints given text.                                 | ``return (0, "Successful")``         |
| 1         | Some problem about arguments. Prints given text.               | ``return (1, "Too much argument.")`` |
| 2         | File directory access error. Prints given text.                | ``return (2, "File not found.")``    |
| 3         | Successful. Don't prints any text. Should take a blank string. | ``return (3, "")``                   |
