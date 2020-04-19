from math import cos, sin
"""
this scripts add numbers , subtracts, divide two numbers
take cos and sin
"""


# addition
def addition_5(*args):
    """
    sums all parameters
    :return: the sum of all parameters
    """

    return sum(args)


# subtration
def subtraction_2(a, b):
    """
    subtracts b from a
    :param a:
    :param b:
    :return: the remainder
    """
    subt = a - b
    return subt


# division
def division_2(a,b):
    """
    divides a by b
    :param a:
    :param b:
    :return: the remainder
    """
    try:
        div_2 = float(a/b)
        return div_2
    except ZeroDivisionError:
        raise ZeroDivisionError


# cosine
def cosine(a):
    """takes cosine"""
    ca = cos(a)
    return ca


# sin
def sine(a):
    """takes sin"""
    si = sin(a)
    return si


def main():
    addition_5()
    subtraction_2()
    division_2()
    sine()
    cosine()


if __name__ == "__main__":
    main()


