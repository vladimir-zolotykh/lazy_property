#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import os
from typing import Literal
import time
from stack_lib import fibonacci

# from recursion_lib import factorial
from stack_lib import factorial

# from recursion_lib import fibonacci


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


class SomeMath:
    @LazyProperty(30)
    def fib(self, n):
        return fibonacci(n)

    @LazyProperty(200)
    def fac(self, n):
        return factorial(n)


class Timer:
    def __init__(self, label=Literal["fibonacci", "factorial"]):
        self.label = label

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.duration = self.end - self.start
        print(f"{self.label:s} elapsed in: {self.duration:.6f} s")


if __name__ == "__main__":
    with Timer("init"):
        somemath = SomeMath()
    with Timer("fibonacci"):
        with open(os.devnull, "w") as dev_null:
            print(somemath.fib, file=dev_null)
    with Timer("factorial"):
        with open(os.devnull, "w") as dev_null:
            print(somemath.fac, file=dev_null)
