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
    coinList = [total + 1] * (total + 1)
    coinList[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            coinList[amount] = min(coinList[amount],
                                   (coinList[amount - coin] + 1))

    if (coinList[total] == total + 1):
        return -1
    return coinList[total]
