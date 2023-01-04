#!/usr/bin/python3
"""
This is a module that containts a clas that avoids
dynmaically created attributes
"""


class LockedClass:
    def __init__(self):
        self.__dict__['first_name'] = None

    def __setattr__(self, name, value):
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
