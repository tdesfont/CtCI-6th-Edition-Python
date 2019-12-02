"""
    Chapter 8: Recursion and Dynamic Programming
    Question 3: Magic Index
"""

def magic_index(array, i=None, j=None):
    if not i and not j:
        i,j = 0, len(array)
    if len(array[i:j]) == 1:
        if not array[i] == i:
            return -1
        else:
            return i
    else:
        middle = (j+i)//2
        if middle < array[middle]:
            return magic_index(array, i, middle)
        elif array[middle] < middle:
            return magic_index(array, middle+1, j)
        else:
            return middle

def magic_index_iter(array):
    i = 0
    j = len(array)
    found = False
    while not found:
        if len(array[i:j]) == 1 and not array[i] == i:
            return -1
        middle = (i+j)//2
        if middle < array[middle]:
            j = middle
        elif array[middle] < middle:
            i = middle+1
        else:
            return middle

if __name__ == "__main__":
    array = [-1, 0, 2, 4, 5, 7, 10]
    assert magic_index(array) == 2
    assert magic_index([3, 8, 9, 9]) == -1
    assert magic_index_iter(array) == 2
    assert magic_index_iter([3, 8, 9, 9]) == -1