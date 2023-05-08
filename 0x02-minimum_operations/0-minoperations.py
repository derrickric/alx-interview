#!/usr/bin/env python3
"""Module for minOperations"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0
    factors = []
    i = 2
    while i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 1
    if not factors:
        return 0
    return sum(factors)

