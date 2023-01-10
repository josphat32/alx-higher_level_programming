#!/usr/bin/python3
'''
    reads a file and print it to stdout
'''


def read_file(filename=""):
    '''
        Reads the contents of a file
    '''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
