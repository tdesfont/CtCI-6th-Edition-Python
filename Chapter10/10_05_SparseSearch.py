def search(strings, string, first, last):
    if first > last:
        return -1
    mid = (last + first)//2
    if not strings[mid]:
        left = mid - 1
        right = mid + 1
        while True:
            if left < first and right > last:
                return -1
            elif right <= last and strings[right]:
                mid = right
                break
            elif left >= first and strings[left]:
                mid = left
                break
            right += 1
            left  -= 1
    if string == strings[mid]:
        return mid
    elif strings[mid] > string:
        return search(strings, string, mid + 1, last)
    else:
        return search(strings, string, first, mid - 1)

if __name__ == "__main__":
    sparseArray = ["at","","","","","","","","ball","","","cr","","","","did","",""]
    print(search(sparseArray, "ball", 0, len(sparseArray)))