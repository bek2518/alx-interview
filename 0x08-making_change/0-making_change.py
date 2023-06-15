#!/usr/bin/python3
'''
Python program that determines the fewest number of coins needed to
meet a given amount total
'''


def makeChange(coins, total):
    '''
    Function that takes list of coins and total amount and determines
    the fewest number of coins needed to meet the total amount
    '''
    if (total <= 0):
        return (0)
    coins.sort(reverse=True)
    counter = 0
    tracker = 0
    for i in range(len(coins)):
        while (tracker <= total):
            tracker = tracker + coins[i]
            counter += 1
            if (tracker == total):
                return counter
            if (tracker > total):
                tracker = tracker - coins[i]
                counter -= 1
                break
    return (-1)
