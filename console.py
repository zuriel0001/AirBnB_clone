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
