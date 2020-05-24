"""dirty"""
import random
import numpy as np

DEFAULT_ACCURACY = 3


def sum_two_values(first, second):
    """returns sum."""
    return first + second


def div(x_val, y_val, accuracy):
    """rounds numbers."""
    return round(x_val / y_val, accuracy)


def get_rand():
    """returns random integer."""
    return random.randint(1, 10)


def rand_array():
    """returns list of random integers."""
    arr = [get_rand(), get_rand(), get_rand()]
    return np.array(arr)


def main():
    """main function."""


main()
