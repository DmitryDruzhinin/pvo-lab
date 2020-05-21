import random
import numpy as np

DEFAULT_ACCURACY = 3


def sum_two_values(first, second):
    return first + second


def div(x_val, y_val, accuracy):
    return round(x_val / y_val, accuracy)


def get_rand():
    return random.randint(1, 10)


def rand_array():
    arr = [get_rand(), get_rand(), get_rand()]
    return np.array(arr)


def main():


main()
