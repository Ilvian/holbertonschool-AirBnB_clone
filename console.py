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
    classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

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

    def help_quit(self):
        """
        Provide help for the 'quit' command.
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Exit the program when Ctrl+D (EOF) is entered.
        """
        return True

    def help_EOF(self):
        """
        Provide help for the 'EOF' command.
        """
        print("EOF command to exit the program.")

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to the JSON file, and prints the ID.

        Args:
            arg (str): The class name for which to create an instance (e.g., "BaseModel").

        Example usage:
        - create BaseModel
        - create
        - create MyModel
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                cls = eval(arg)
                inst = cls()
                inst.save()
                print(inst.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show the string representation of an instance.
        """
        args = arg.split()
        if len(args) != 2:
            print("** missing class name or instance id **")
            return

        class_name, instance_id = args[0], args[1]
        try:
            cls = eval(class_name)
            instance = storage.get(cls, instance_id)
            if instance:
                print(instance)
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.

        Args:
            arg (str): Class name and instance ID in the format "class_name instance_id."

        Example usage:
        - destroy BaseModel 1234-1234-1234
        """
        args = arg.split()
        if len(args) != 2:
            print("** missing class name or instance id **")
            return

        class_name, instance_id = args[0], args[1]
        try:
            cls = eval(class_name)
            instance = storage.get(cls, instance_id)
            if instance:
                storage.delete(instance)
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representations of instances based on the class name.

        Args:
            arg (str): The class name (optional).

        Example usage:
        - all BaseModel
        - all
        """
        if arg:
            try:
                cls = eval(arg)
                instances = storage.all(cls).values()
            except NameError:
                print("** class doesn't exist **")
                return
        else:
            instances = storage.all().values()

        print([str(instance) for instance in instances])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating an attribute.

        Args:
            arg (str): Class name, instance ID, attribute name, and attribute value in the format "class_name instance_id attribute_name 'attribute_value'."

        Example usage:
        - update BaseModel 1234-1234-1234 email 'aibnb@mail.com'
        """
        args = arg.split()
        if len(args) < 3:
            print("** missing class name, instance id, attribute name, or value **")
            return

        class_name, instance_id, attribute_name = args[0], args[1], args[2]
        try:
            cls = eval(class_name)
            instance = storage.get(cls, instance_id)
            if instance:
                if len(args) >= 4:
                    setattr(instance, attribute_name, args[3][1:-1])
                    instance.save()
                else:
                    print("** value missing **")
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
