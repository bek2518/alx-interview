#!/usr/bin/python3
'''
Python program that determines the perimeter of the island described
in grid
'''


def island_perimeter(grid):
    '''
    Function that returns the perimeter of the island by taking
    grid as an argument
    '''
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                counter += 1

    overlap = (counter - 1) * 2
    totalSides = counter * 4
    perimeter = totalSides - overlap
    return (perimeter)
