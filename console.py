#!/usr/bin/python3
"""
This module implements a basic command-line interface for the hbnb application.
"""

import cmd
import re
from models.base_model import BaseModel
from models import storage


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
    def do_create(self, arg):
        """create BaseModel"""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            create = storage.classes()[arg]()
            create.save()
            print(create.id) 

    def do_show(self, args):
        """show BaseModel"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            words = arg.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """destroy BaseModel"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            words = arg.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representations of instances
        filtered by class name if provided."""
        # Check if the line is not empty after stripping whitespace
        if line.strip():
            args = line.split()
            class_name = args[0]
            # Check if the class exists in storage
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                # Collect and print instances of the specified class
                filtered_instances = [
                    str(obj) for obj in storage.all().values()
                    if type(obj).__name__ == class_name
                ]
                print(filtered_instances)
        else:
            # Collect and print all instances
            all_instances = [str(obj) for obj in storage.all().values()]
            print(all_instances)

    def do_update(self):
        """update BaseModel"""
        if line == "" or line is None:
            print("** class name missing **")
            return

        # Regular expression to parse the input line
        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = f"{classname}.{uid}"
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                # Determine the type of the value
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # If casting fails, keep it as a string
                
                # Update the attribute and save the instance
                instance = storage.all()[key]
                setattr(instance, attribute, value)
                instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
