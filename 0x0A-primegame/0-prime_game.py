#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    This function predicts the winner of prime number game.

    The game goes like this:
    n numbers are given in an array, each of two players
    picks a prime number, and all multiples of that number
    get eliminated from the list. The player who can't pick
    a prime number anymore loses the game.

    assume the two players are Maria and Ben, and Maria goes first.

    Args:
        x: number of rounds
        nums: list of n numbers
    """

    if not nums or x < 1:
        return None

    n = max(nums)

    prime = [True for i in range(max(n + 1, 2))]
    p = 2
    while p * p <= n:
        if prime[p] is True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    prime[0] = prime[1] = False

    c = 0
    for i in range(len(prime)):
        if prime[i]:
            c += 1
        prime[i] = c

    winner = 0
    for n in nums:
        winner ^= prime[n] % 2

    if winner == 0:
        return "Ben"
    return "Maria"
