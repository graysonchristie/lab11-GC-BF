"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def logarithm(x, base):
    if x <= 0:
        raise ValueError("log argument must be positive")
    if base <= 0 or base == 1:
        raise ValueError("invalid log base")
    return math.log(x, base)

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(x)

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)