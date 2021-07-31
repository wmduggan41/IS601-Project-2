import math

# Static Methods:
def n_sigfig(a, n):
    sigfig = math.floor(math.log(a, 10)) + 1  # number of significant digits in value
    return round(a, n - sigfig + 1)  # returns value to "n" significant figures


def addition(a, b):
    return int(a) + int(b)


def division(a, b):
    return float(b) / float(a)


def multiplication(a, b):
    return int(a) * int(b)


def square(a):
    return int(a) ** 2


def square_root(a):
    return math.sqrt(int(a))


def subtraction(a, b):
    return int(b) - int(a)