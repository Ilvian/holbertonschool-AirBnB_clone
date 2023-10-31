#!/usr/bin/env python3
"""
Console module for your project.
"""


import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    classes = {
            "BaseModel": BaseModel
    }

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit the console"""
        return True

    def do_EOF(self, arg):
        """Exit on EOF (Ctrl+D)"""
        return True

    def do_create(self, arg):
        """
        Create a new instance of a class, save it, and print the id.
        """
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg.split()[0]
            if class_name in self.classes:
                new_instance = self.classes[class_name]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")


    def do_show(self, arg):
        """
        Print the string representation of an instance based on class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            if class_name in self.classes:
                instances = models.storage.all()
                instance_key = "{}.{}".format(class_name, instance_id)
                instance = instances.get(instance_key)
                if instance:
                    print(instance)
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on class name and id (save changes to the JSON file)."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            if class_name in self.classes:
                instances = self.classes[class_name].all()
                if instance_id in instances:
                    del instances[instance_id]
                    self.classes[class_name].save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances, based on class name or not."""
        args = arg.split()
        if not args:
            print([str(instance) for cls in self.classes.values() for instance in cls.all().values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on class name, id, attribute name, and value (save changes to the JSON file)."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]
            if class_name in self.classes:
                instance = self.classes[class_name].get(instance_id)
                if instance:
                    if hasattr(instance, attribute_name):
                        attr_type = type(getattr(instance, attribute_name))
                        setattr(instance, attribute_name, attr_type(attribute_value))
                        instance.save()
                    else:
                        print("** attribute doesn't exist **")
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

