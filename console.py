#!/usr/bin/python3


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def emptyline(self):
        pass

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
