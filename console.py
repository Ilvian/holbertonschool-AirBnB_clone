#!/usr/bin/python3


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
        pass

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
    """
    Check if the code is being executed directly (not imported).
    Create an instance of the HBNBCommand class and start the command loop.
    """
    HBNBCommand().cmdloop()
