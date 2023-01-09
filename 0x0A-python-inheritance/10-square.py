#!/usr/bin/python3
'''
    Implementing a Geometry class
'''

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''
        Implementing the class Square
    '''
    def __init__(self, size):
        '''
            init class
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''
            finds area of the square
        '''
        return (self.__size ** 2)
