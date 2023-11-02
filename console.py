#!/usr/bin/python3
'''
Module to create a console to add interactivity to our
project where admin users can update add delete
'''


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''
    Console class to create a
    console which will take differenct
    commands and execute them
    '''
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on an empty line
        """
        pass

    def default(self, line):
        """
        Handle dynamic class commands
        """
        args = line.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        if args[1] == "all":
            self.do_all(class_name)
        elif args[1] == "show":
            self.do_show(class_name + " " + args[2])
        elif args[1] == "create":
            self.do_create(class_name)
        elif args[1] == "destroy":
            self.do_destroy(class_name + " " + args[2])
        elif args[1] == "update":
            self.do_update(class_name + " " + " ".join(args[2:]))

    def do_create(self, class_name):
        """
        Create a new instance of a specified class and save it
        """
        if not class_name:
            print("** class name missing **")
            return

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])
        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, class_name):
        """
        Print all string representations of instances
        """
        if not class_name:
            print([str(val) for val in storage.all().values()])
        else:
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            result = [
                    str(val)
                    for key, val in storage.all().items()
                    if key.startswith(class_name)
                    ]
            print(result)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])
        if key not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            instance = storage.all()[key]
            setattr(instance, args[2], args[3])
            instance.save()


if __name__ == '__main__':
    """infinite loop"""
    HBNBCommand().cmdloop()
