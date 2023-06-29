#!/usr/bin/python3
'''
Python program that determines the winner of the game prime number
played between two players
'''
import sys
sys.setrecursionlimit(10**6)


def isWinner(x, nums):
    '''
    Function that determines the winner from maria and ben, where they
    play x number of games and nums is a list of n which is the set of
    consecutive integers starting from 1 upto and including n
    '''
    Maria = 0
    Ben = 0

    for i in range(0, x):
        currentPlayer = 'Maria'
        integers = []

        for j in range(1, nums[i] + 1):
            integers.append(j)

        roundWinner = recursiveFunction(integers, currentPlayer)

        if roundWinner == 'Maria':
            Maria += 1
        elif roundWinner == 'Ben':
            Ben += 1

    if (Maria > Ben):
        return('Maria')
    elif (Ben > Maria):
        return('Ben')
    else:
        return(None)


def switchPlayer(currentPlayer):
    '''
    Function that swiches from one player to the other
    '''
    if (currentPlayer == 'Maria'):
        return('Ben')
    return ('Maria')


def recursiveFunction(integers, currentPlayer):
    '''
    Recursive function that removes a number and its multiples
    till only one remains
    '''
    if (len(integers) > 1):
        toBeDeleted = []
        for i in range(len(integers)):
            if ((integers[i] % integers[1]) == 0):
                toBeDeleted.append(integers[i])

        for i in range(len(toBeDeleted)):
            integers.remove(toBeDeleted[i])

        currentPlayer = switchPlayer(currentPlayer)
        return(recursiveFunction(integers, currentPlayer))

    currentPlayer = switchPlayer(currentPlayer)
    return (currentPlayer)
