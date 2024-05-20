#!/usr/bin/python3
"""Class Definition."""
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
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show string representation of an instance."""

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        cls_name, cls_id = args
        key = f"{cls_name}.{cls_id}"
        try:
            obj = storage.all()[key]
            print(obj)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        cls_name, cls_id = args
        key = f"{cls_name}.{cls-id}"
        if key in storge.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all strings representation of instances."""

        if arg:
            try:
                cls = eval(arg)
                obj_list = [
                        str(obj) for obj in storage.all().values() if isinstance(obj, cls)]
            except NameError:
                print("** class doesn't exist **")
                return
        else:
            obj_list = [str(obj) for obj in storage.all().values()]
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        cls_name, cls_id, attr_name, attr_value = args
        key = f"{cls_name}.{cls_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        obj = storage.all()[key]
        try:
            attr_value = eval(attr_value)
        except (SyntaxError, NameError):
            pass
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
