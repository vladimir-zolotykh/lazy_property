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
>>> fibonacci(7)
13

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
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
