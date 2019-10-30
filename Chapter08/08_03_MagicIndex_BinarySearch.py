def magicFast(array, start=None, end=None):
    if (start is None) or (end is None):
        return magicFast(array, 0, len(array)-1)
    if end < start:
        return -1
    mid = (start+end)//2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return magicFast(array, start, mid-1)
    else:
        return magicFast(array, mid+1, end)

if __name__ == "__main__":
    A = [-40, -20, -1, 3, 7]
    print(magicFast(A))