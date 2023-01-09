#!/usr/bin/python3
'''
    Class that takes an integers
'''


class MyInt(int):
    '''
        Implements integer class
    '''
    def __init__(self, number):
        '''
            Initialize numbers
        '''
        self.number = number

    def __ne__(self, val):
        '''
            number equal
        '''
        return (self.number == val)

    def __eq__(self, val):
        '''
            Number not equal
        '''
        return (self.number != val)

    def __str__(self):
        '''
            returns the number
        '''
        return (str(self.number))
