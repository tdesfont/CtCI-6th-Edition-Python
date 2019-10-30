def mergeSort(array, helper, low, high):
    if not helper:
        helper = [None for i in range(len(array))]
    if low < high:
        middle = int((low + high)/2)
        mergeSort(array, helper, low, middle)
        mergeSort(array, helper, middle+1, high)
        merge(array, helper, low, middle, high)

def merge(array, helper, low, middle, high):
    for i in range(low, high+1):
        helper[i] = array[i]
    helperLeft = low
    helperRight = middle + 1
    current = low

    while (helperLeft <= middle and helperRight <= high):
        if helper[helperLeft] <= helper[helperRight]:
            array[current] = helper[helperLeft]
            helperLeft += 1
        else:
            array[current] = helper[helperRight]
            helperRight += 1
        current += 1

    remaining = middle - helperLeft
    for i in range(remaining+1):
        array[current + i] = helper[helperLeft + i]

if __name__ == "__main__":
    A = [3, 1, 2, 8, 3, 4]
    print("Return sorted array:", A)