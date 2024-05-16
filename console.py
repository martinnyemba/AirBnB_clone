#!/usr/bin/python3
"""
This module implements a basic command-line interface for the hbnb application.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """
    # A custom prompt: (hbnb)
    prompt = "(hbnb)"
    
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    # Update command interpreter (console.py) Task: 7. Console 0.1
    def do_create(self):
        """create BaseModel"""
        pass

    def do_show(self):
        """show BaseModel"""
        pass

    def do_destroy(self):
        """destroy BaseModel"""
        pass

    def do_all(self):
        """all BaseModel"""
        pass
    def do_update(self):
        """update BaseModel"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
