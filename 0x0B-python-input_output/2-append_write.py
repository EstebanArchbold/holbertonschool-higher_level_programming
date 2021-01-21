#!/usr/bin/python3
"""
Defining append_write Function
"""


def append_write(filename="", text=""):
    '''
    Function that appends a string at the end of a text file
    '''
    with open(filename, mode="a", encoding="UTF-8") as fl:
        return fl.write(text)
