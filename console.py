#!/usr/bin/python3
"""
This module implements a basic command-line interface for the hbnb application.
"""

import sys


class Console:
    """
    This class represents the command-line interface for the hbnb application.
    """

    def __init__(self):
        pass

    def help(self):
        """
        Display the list of available commands.
        """
        print("Documented commands (type help <topic>):")
        print("=" * 40)
        print("EOF  help  quit")

    def run(self):
        """
        Run the command-line interface.
        """
        print("(hbnb)")
        for line in sys.stdin:
            command = line.strip()
            if command == "help":
                self.help()
            elif command == "quit":
                break
            else:
                print("Invalid command. Type 'help' for available commands.")
        print()


if __name__ == "__main__":
    console = Console()
