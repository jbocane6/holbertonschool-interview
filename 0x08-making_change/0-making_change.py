#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins: list, total: int) -> int:
    """
    First, sort coins in a descendent way
    Then calculate the less amount of coins
    by dividing total by the value of the coins.
    Return: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0

    amount = 0
    coins.sort(reverse=True)

    for coin in coins:
        if total // coin > 0:
            amount += total // coin
            total = total % coin
        if total == 0 and amount > 0:
            return amount
    return -1
