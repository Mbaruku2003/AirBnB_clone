#!/usr/bin/python3
import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """Prompt for file."""

    prompt = "(hbnb) "

    def do_quit(sef, arg):
        """Quit command to exit the program."""

        return True

    def do_EOF(self, arg):
        """Exit the program."""

        return True

    def emptyline(self):
        """Empty line."""

        pass

    def do_create(self, arg):
        """Creates aninstance of basemdel."""

        if not arg:
            print("*** class name missing ***")
            return
        if arg not in storage.classes:
            print("** class doesn't exist **")
            return
        obj = storage.classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Show string representation of an instance."""

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            print(storage.all[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all strings representation of instances."""

        if arg and arg not in storage.classes:
            print("** class doesn't exist **")
            return
        objs = [str(obj) for key, obj in storage.all().items() if not arg or arg == key.split('.')[0]]
        print(objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating an attribute."""

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            setattr(obj, attr_name, attr_type(attr_value))
            obj.save()
        else:
            print("** attribute not found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
