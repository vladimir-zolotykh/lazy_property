#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class LazyProperty:
    def __init__(self, arg):
        self.arg = arg

    def __call__(self, func):
        self.func = func
        self.name = "_" + func.__name__
        return self

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        if not hasattr(instance, self.name):
            setattr(instance, self.name, self.func(instance, self.arg))
        return getattr(instance, self.name)


def fibonacci(n):
    if n in (0, 1):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


class SomeMath:
    @LazyProperty(30)
    def fib(self, n):
        return fibonacci(n)

    @LazyProperty(50)
    def fac(self, n):
        return factorial(n)


if __name__ == "__main__":
    somemath = SomeMath()
    print(somemath.fib)
    print(somemath.fac)
