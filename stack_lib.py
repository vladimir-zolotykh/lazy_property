#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> fibonacci(0)
0
>>> fibonacci(1)
1
>>> fibonacci(2)
1
>>> fibonacci(3)
2
>>> fibonacci(4)
3
>>> fibonacci(5)
5
>>> fibonacci(6)
8

>>> factorial(0)
1
>>> factorial(1)
1
>>> factorial(2)
2
>>> factorial(3)
6
>>> factorial(4)
24
>>> factorial(5)
120
"""


def fibonacci(n):
    """
    Returns the nth Fibonacci number using an explicit stack (iterative approach).
    F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2, etc.

    Args:
        n (int): Non-negative integer

    Returns:
        int: The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    # Initialize stack with the base cases: [1, 1] represents F(2), F(1)
    stack = [1, 1]  # stack[-1] is the latest Fibonacci number

    # We need to compute up to F(n), we've already done F(1) and F(2)
    for i in range(3, n + 1):
        next_fib = stack[-1] + stack[-2]  # F(i) = F(i-1) + F(i-2)
        stack.append(next_fib)  # Push the new value onto the stack

    return stack[-1]


def factorial(n):
    """return n * factorial(n - 1)"""
    if n in (0, 1):
        return 1
    stack = [1]
    for i in range(1, n + 1):
        next_fac = i * stack[-1]
        stack.append(next_fac)
    return stack[-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
