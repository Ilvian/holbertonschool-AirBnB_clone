#!/usr/bin/python3
"""
This is the console.py script for the HBNB command interpreter.
It provides a simple command-line interface for interacting with the program.
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    Custom command interpreter class.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        return False

    def do_quit(self, arg):
        """
        Exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when Ctrl+D (EOF) is entered.
        """
        return True

    def help_quit(self):
        """
        Provide help for the 'quit' command.
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Provide help for the 'EOF' command.
        """
        print("EOF command to exit the program.")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
