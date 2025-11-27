#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


def fibonacci(n):
    if n in (0, 1):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)
