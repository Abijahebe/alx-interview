#!/usr/bin/python3

"""
    Method that determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
    Returns the number of operations needed to get n H characters
    """
    if n <= 1:
        return 0

    counter = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            counter += divisor
            n = n // divisor
        divisor += 1

    return counter
