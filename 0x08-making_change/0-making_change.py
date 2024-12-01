#!/usr/bin/python3
"""A function that finds the minimum coin combination"""


def makeChangeRecurr(total, index, pool):
    """
    A recursive function that carries out the algorithm
    for determining the minimum sum of coins to make up
    a desired total

    Arguments:
        total: The desired total
        index: index of the current value in @pool
        pool: The available coin denominations
        invalid: true if no possible combination
    """
    if index == len(pool):
        return -1000000000000
    rem = total % pool[index]

    if rem == 0:
        return total // pool[index]
    if rem == total:
        return makeChangeRecurr(total, index + 1, pool)
    else:
        return (total // pool[index]) +\
                makeChangeRecurr(total % pool[index], index, pool)


def makeChange(coins, total):
    """
    This function returns the minimum number of coins
    whose sum makes up a desired total

    Arguments:
        coins: A list of all available denominations
        total: The desired amount
    Note:
        It is assumed each unique number in @coins
        appears infinite times
    """
    if total <= 0:
        return 0
    if len(coins) == 0:
        return -1

    coins.sort(reverse=True)
    num = makeChangeRecurr(total, 0, coins)
    if num < 0:
        return -1
    return num
