"""Dirty"""
import random
import numpy as np

DEFAULT_ACCURACY = 3


def sum_two_values(first, second):
    """Returns sum."""
    return first + second


def div(x_val, y_val, accuracy):
    """Rounds numbers."""
    return round(x_val / y_val, accuracy)


def get_rand():
    """Returns random integer."""
    return random.randint(1, 10)


def rand_array():
    """Returns list of random integers."""
    arr = [get_rand(), get_rand(), get_rand()]
    return np.array(arr)


def main():
    """Main function."""


main()
