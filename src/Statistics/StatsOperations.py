from Operations import *


def mean(data):
    count = len(data)
    total = 0
    for num in data:
        total = addition(total, num)
    return division(count, total)


def median(data):
    # sort data
    data.sort()
    # odd length, means true midpoint
    if len(data) % 2 != 0:
        mid = len(data) // 2
        return data[mid]
    # even length, means avg midpoints
    else:
        mid_left = len(data) // 2
        mid_right = mid_left + 1
        return division(addition(data[mid_left], data[mid_right]), 2)


def mode(data):
    # guess initial mode value
    current_mode = data[0]
    current_max = -1
    # iterate over data and find latest mode
    for elem in data:
        if data.count(elem) >= current_max:
            current_mode = elem
            current_max = data.count(elem)
    return current_mode


def variance(data):
    n = len(data)
    x_bar = mean(data)
    sum_squared = 0
    for x_i in data:
        sum_squared += square(x_i - x_bar)

    return division(n-1, sum_squared)


def std_dev(data):
    return square_root(variance(data))
