#!/usr/bin/python3
'''
Python program that rotates a given 2D matrix 90 degree clockwise
'''


def rotate_2d_matrix(matrix):
    '''
    Function that takes in an nxn mtrix and rotates it 90 degrees
    '''
    temp_matrix = []
    n = len(matrix)
    for i in range(n):
        temp_matrix.append([0] * n)

    last = n - 1
    for i in range(n):
        for j in range(n):
            temp_matrix[j][last] = matrix[i][j]
        last -= 1

    for i in range(n):
        for j in range(n):
            matrix[i][j] = temp_matrix[i][j]
