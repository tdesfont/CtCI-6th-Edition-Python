def binarySearch(array, x):
    low = 0
    high = len(array) - 1
    mid = None

    while low <= high:
        mid = (low + high)//2
        if array[mid] < x:
            low = mid + 1
        elif array[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def binarySearchRecursive(array, x, low, high):
    if low > high:
        return -1
    mid = (low + high)//2
    if array[mid] < x:
        return binarySearchRecursive(array, x, mid + 1, high)
    elif array[mid] > x:
        return binarySearchRecursive(array, x, low, mid-1)
    else:
        return mid

if __name__ == "__main__":
    A = [1, 3, 5, 8, 9, 10, 18, 20, 28, 30, 32, 34]
    print(binarySearch(A, 18))
    print(binarySearchRecursive(A, 18, 0, len(A)))