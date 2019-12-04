"""
    Bubble Sort
"""

import random

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j+1] < array[j]:
                swap(array, j, j+1)
    return array

if __name__ == "__main__":
    array = [random.randint(0, 10) for i in range(20)]
    print("Initial list:", array)
    print(bubble_sort(array))