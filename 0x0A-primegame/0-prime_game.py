#!/usr/bin/python3
""" Maria and Ben are playing a game.
Given a set of consecutive integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and removing that number
and its multiples from the set.
The player that cannot make a move loses the game.
They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.

    Prototype: def isWinner(x, nums)
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task
"""


def isWinner(x, nums):
    """Prime game"""
    if x < 1 or not nums:
        return None
    n = max(nums)
    primes = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not primes[i]:
            continue
        for j in range(i * i, n + 1, i):
            primes[j] = False
    primes[0] = primes[1] = False
    c = 0
    for i in range(len(primes)):
        if primes[i]:
            c += 1
        primes[i] = c
    turns = 0
    for n in nums:
        turns += primes[n] % 2 == 1
    if turns * 2 == len(nums):
        return None
    if turns * 2 > len(nums):
        return "Maria"
    return "Ben"
