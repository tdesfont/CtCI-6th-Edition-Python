"""
    16.7 Number Max
"""

from math import log, floor

def getMax(a, b):
    """
        Return the boolean predicate a is greater than b
    :param a:
    :param b:
    :return:
    """
    c = a^b
    return c != 0 and bool(( 1 << floor(log(c)/log(2))) & a)

if __name__ == "__main__":
    tuples = [(11, 5), (0, 0), (3, 9)]
    for a, b in tuples:
        print(a, b, getMax(a, b))