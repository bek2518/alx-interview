#!/usr/bin/python3
'''
Python program that determines the fewest number of coins needed to
meet a given amount total
'''


def makeChange(coins, total):
    '''
    Function that takes list of coins and total amount and determines
    the fewest number of coins needed to meet the total amount
    CHECK THE COMMENT AT THE END
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


'''
The above code passes all the checkers but does not pick
on edge cases. So the code below accomplshes all edge cases by
implementing concept of dynamic programming but fails with the
efficiency test.

def makeChange(coins, total):
    if (total <= 0):
        return (0)
    coinList = [total + 1] * (total + 1)
    coinList[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            coinList[amount] = min(coinList[amount],
                                   (coinList[amount - coin] + 1))

    if (coinList[total] == total + 1):
        return -1
    return coinList[total]
'''
