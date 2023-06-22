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
    overlapCounterList = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                overlapCounter = 0
                if (i > 0):
                    if grid[i - 1][j] == 1:
                        overlapCounter += 1
                if (i < (len(grid) - 1)):
                    if grid[i + 1][j] == 1:
                        overlapCounter += 1
                if (j > 0):
                    if grid[i][j - 1] == 1:
                        overlapCounter += 1
                if (j < (len(grid[i]) - 1)):
                    if grid[i][j + 1] == 1:
                        overlapCounter += 1
                counter += 1
                overlapCounterList.append(overlapCounter)
            overlapCounter = 0
    overlap = sum(overlapCounterList)
    totalArea = counter * 4
    perimeter = totalArea - overlap
    return perimeter
