#!/usr/bin/python3
'''
    Checks if the object is exactly an instance of specified class
'''


def is_same_class(obj, a_class):
    '''
        Check if the objects have the same class
    '''
    if type(obj) is a_class:
        return True
    return False
