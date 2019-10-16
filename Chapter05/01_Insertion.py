"""
	Chapter 5. Bit Manipulation
		5.1 Insertion
"""

from math import log, ceil, floor

def get_bits(n):
    return floor(log(n)/log(2))+1

def insert(M, N, i, j):
    len_bits = get_bits(N)
    mask = ((2**len_bits-1)<<(j+1))%(2**len_bits) + (2**i-1)
    return (N & mask) | (M << i)

if __name__ == '__main__':
    M = int("10011", 2)
    N = int("10000000000", 2)
    r = insert(M, N, i=2, j=6)