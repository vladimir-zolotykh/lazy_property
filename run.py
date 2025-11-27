#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from typing import Literal
import time
import math

# from stack_lib import fibonacci

# from recursion_lib import factorial

# from stack_lib import factorial

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
    def __init__(
        self, lib_name: Literal["stack_lib", "recursion_lib"] = "recursion_lib"
    ):
        self.lib_name = lib_name
        if lib_name == "stack_lib":
            from stack_lib import fibonacci, factorial
        elif lib_name == "recursion_lib":
            from recursion_lib import fibonacci, factorial  # noqa F401
        else:
            raise ValueError("Expected stack_lib or recursion_lib")
        self.fibonacci = fibonacci
        self.factorial = factorial

    @LazyProperty(30)
    def fib(self, n):
        return self.fibonacci(n)

    @LazyProperty(200)
    def fac(self, n):
        return self.factorial(n)


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
        somemath = SomeMath("stack_lib")
    with Timer("fibonacci"):
        assert somemath.fib == 832040
    with Timer("factorial"):
        assert somemath.fac == math.factorial(200)
