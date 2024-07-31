import numpy as np


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    # This function takes two numbers a and b and multiplies them and returns the result.
    return a * b


def mean(numbers):
    return np.mean(numbers)


numbers = [1, 2, 3]

print(mean(numbers))
print(add(1, 2))
print(substract(5, 3))
print(multiply(2, 2))
