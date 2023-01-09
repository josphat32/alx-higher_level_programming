#!/usr/bin/python3
'''
    returns the list of available attributes and methods of an object
'''


def lookup(obj):
    '''
        Returns a list of avaiblable attributes and methods in the object
    '''
    return (dir(obj))
