"""
	Chapter 5. Bits Manipulation
	5.3 Flip Bit to Win
"""

from math import floor, log

def get_bit(n, i):
    return (n>>i)&1

def flipToWin(n):
    n_bits = floor(log(n)/log(2))+1
    s = max_s = 0
    window_left, window_right = -1
    for i in range(0, n_bits):
        s += 1
        if get_bit(n, i):
            s -= (window_left - window_right)
            window_left, window_right = i, window_left
        if s > max_s:
            max_s = s
        return max_s