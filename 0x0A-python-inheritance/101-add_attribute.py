#!/usr/bin/python3
def add_attribute(obj, att, value):
    '''
        adds new attribute

    if not hasattr(cls, name):
        raise TypeError("can't add new attribute")
    cls.name = first
    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
