"""
    Selection Sort
"""

import random

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def selection_sort(array):
    for i in range(len(array)-1):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        swap(array, i, min_index)
    return array

if __name__ == "__main__":
    array = [random.randint(0, 10) for i in range(20)]
    print("Initial array:\n", array)
    print("Final array:\n", selection_sort(array))
