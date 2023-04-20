#!/usr/bin/python3
'''
Create a function that returns a list of lists of
integers representing pascal's triangle
'''
from math import factorial


def pascal_triangle(n):
    '''
    Function that returns list of lists
    '''
    inner_list = []
    outer_list = []
    if (n <= 0):
        return (outer_list)

    for i in range(n):
        inner_list = []
        for j in range(i + 1):
            inner_list.append(factorial(i)//(factorial(j)*factorial(i-j)))
        outer_list.append(inner_list)
    return outer_list
