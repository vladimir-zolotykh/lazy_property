#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class LazyProperty:
    def __init__(self, func):
        self.func = func
        self._name = func.__name__

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        instance.__dict__[self._name] = self.func(instance)
        return instance.__dict__[self._name]


def fibonacci(n):
    if n in (0, 1):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


class SomeMath:
    @LazyProperty
    def fib(self):
        return fibonacci(30)

    @LazyProperty
    def fac(self):
        return factorial(50)


if __name__ == "__main__":
    somemath = SomeMath()
    print(somemath.fib)
    print(somemath.fac)
