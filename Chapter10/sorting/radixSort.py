"""
    Radix Sort: O(k.n) where n is the number of elements and k is the number of passes of the sorting algorithm
"""

from math import log, floor
from queue import deque

def getBit(n, i):
    """
        Must return 0 or 1
    :param n:
    :param i:
    :return:
    """
    return (n &(1<<i))>>i

def radixSort(array, bound):
    """
    Assuming that all elements in the array are integers lower to bound
    :param array:
    :param bound:
    :return:
    """
    nbit = floor(log(bound)/log(2))+1
    return radixSortHelper(array, nbit, 0, len(array))

def radixSortHelper(array, nbit, left, right):
    if left < right and nbit >= 0:
        count = 0
        helper = deque()
        for i in range(left, right):
            element = array[i]
            if getBit(element, nbit):
                helper.append(element)
            else:
                helper.appendleft(element)
                count += 1
        for i in range(0, len(helper)):
            array[i+left] = helper[i]
        radixSortHelper(array, nbit-1, left, left+count)
        radixSortHelper(array, nbit-1, left+count+1, right)

if __name__ == "__main__":
    A = [13, 4, 2, 9, 1, 2, 3, 8, 1, 7, 3]
    radixSort(A, 13)
    print(A)