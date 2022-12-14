#!/usr/bin/python3
'''
    Defines a Rectangle
'''


class Rectangle:
    '''
        Represents Rectangle
    '''
    def __init__(self, width=0, height=0):
        '''
           Calling the setters to initialize the instance variables
        '''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''
            Returning the private var
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
           Checking for TypeError and ValueError
           then setting up the private var
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
           Returning the private var
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Checking for TypeError and ValueError
            then setting up the private var
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
