# Grammar test file for Python 3.14
# Tests various Python syntax features that semshi should handle

# Basic assignments
x = 1
y = "hello"
z = [1, 2, 3]

# Function definitions
def simple_func(a, b, c=10):
    return a + b + c

async def async_func(x, y):
    return x + y

# Lambda
square = lambda x: x * x

# Class definition
class MyClass:
    def __init__(self, value):
        self.value = value

    def method(self):
        return self.value

# Comprehensions (inlined in 3.12+)
list_comp = [x for x in range(10)]
set_comp = {x for x in range(10)}
dict_comp = {x: x*2 for x in range(10)}
gen_exp = list(x for x in range(10))

# Nested comprehensions
nested = [[y for y in range(x)] for x in range(5)]

# Try/except/else/finally
try:
    result = 1 / 0
except ZeroDivisionError as e:
    result = 0
else:
    pass
finally:
    cleanup = True

# Match/case (3.10+)
match x:
    case 1:
        val = "one"
    case 2:
        val = "two"
    case _:
        val = "other"

# Walrus operator (3.8+)
if (n := 10) > 5:
    big = True

# F-strings
name = "world"
greeting = f"hello {name}"

# Positional-only parameters (3.8+)
def pos_only(a, b, /, c, d):
    return a + b + c + d

# Global/nonlocal
g = 100
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
    global g
    g = 200

# Import
import os
from os import path
from os.path import join as pjoin

# Decorators
def decorator(func):
    return func

@decorator
def decorated():
    pass

# Star expressions
first, *rest = [1, 2, 3, 4]

# Yield
def gen():
    yield 1
    yield from range(10)

# Async for/with
async def async_features():
    pass

# Exception groups (3.11+)
try:
    pass
except* ValueError as eg:
    pass
except* TypeError as eg:
    pass
