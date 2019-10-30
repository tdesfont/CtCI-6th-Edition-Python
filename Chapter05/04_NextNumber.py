from math import log, ceil, floor

def bits_nbr(n):
    return floor(log(n)/log(2))+1

def get_bit(n, i):
    return (n>>i)&1

def set_bit(n, b):
    mask = bits_nbr(n)
    mask = mask &

