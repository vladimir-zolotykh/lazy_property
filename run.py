#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from typing import Literal
import time
import math
import argcomplete
import argparse
import logging

logging.basicConfig(level=logging.INFO)
LP_logger = logging.getLogger(__name__ + ".LazyProperty")


class LazyProperty:
    def __init__(self, arg):
        LP_logger.info(f"{arg = }")
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
    FACTORIAL_ARG = 200
    FIBONACCI_ARG = 30

    def __init__(
        self,
        lib_name: Literal["stack_lib", "recursion_lib"] = "recursion_lib",
        fac_arg=None,
        fib_arg=None,
    ):
        self.lib_name = lib_name
        if fac_arg is not None:
            self.fac_arg = fac_arg
        if fib_arg is not None:
            self.fib_arg = fib_arg
        if lib_name == "stack_lib":
            from stack_lib import fibonacci, factorial
        elif lib_name == "recursion_lib":
            from recursion_lib import fibonacci, factorial  # noqa F401
        else:
            raise ValueError("Expected stack_lib or recursion_lib")
        self.fibonacci = fibonacci
        self.factorial = factorial

    @LazyProperty(FIBONACCI_ARG)
    def fib(self, n):
        return self.fibonacci(n)

    @LazyProperty(FACTORIAL_ARG)
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


parser = argparse.ArgumentParser(
    description="Lazy property demo",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "--lib-name",
    choices=["recursion_lib", "stack_lib"],
    default="stack_lib",
    help="recursion or stack",
)
parser.add_argument("--fib-arg", type=int, default=30, help="Fibonacci arg")
parser.add_argument("--fac-arg", type=int, default=200, help="Factorial arg")

argcomplete.autocomplete(parser)
if __name__ == "__main__":
    args = parser.parse_args()
    with Timer("init"):
        somemath = SomeMath(args.lib_name, fac_arg=args.fac_arg, fib_arg=args.fib_arg)
    with Timer("fibonacci"):
        assert somemath.fib == 832040
    with Timer("factorial"):
        assert somemath.fac == math.factorial(200)
