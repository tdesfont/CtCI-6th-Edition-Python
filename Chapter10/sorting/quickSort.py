def quickSort(array, left, right):
    index = partition(array, left, right)
    if left < index - 1:
        quickSort(array, left, index - 1)
    if index < right:
        quickSort(array, index, right)

def partition(array, left, right):
    pivot = array[int((left+right)/2)]
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            swap(array, left, right)
            left += 1
            right -= 1
    return left

def swap(array, left, right):
    array[left], array[right] = array[right], array[left]

if __name__ == "__main__":
    A = [8, 4, 2, 8, 9, 3, 2]
    quickSort(A, 0, len(A)-1)
    print(A)