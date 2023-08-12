#!/usr/bin/python3
"""Functions that defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    my_curly_braces = re.search(r"\{(.*?)\}", arg)
    my_brackets = re.search(r"\[(.*?)\]", arg)
    if my_curly_braces is None:
        if my_brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:my_brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(my_brackets.group())
            return retl
    else:
        lexer = split(arg[:my_curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(my_curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Class that defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Pass upon receiving an empty line."""
        pass

    def default(self, arg):
        """The Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False
