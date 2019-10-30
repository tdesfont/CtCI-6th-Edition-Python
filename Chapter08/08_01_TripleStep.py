# TODO: Compare the Time and Space Complexity using Recursive Approach and Dynamic Programming

def getArray(array, i):
    if i >= 0 and i < len(array):
        return array[i]
    else:
        return None

def tripleStep(n):
    array = [0 for i in range(n)]
    array[0] = 1
    for i in range(0, n):
        for j in range(1, 4):
            element = getArray(array, i-j)
            if element:
                array[i] += element
    print(array)
    return array[n-1]

if __name__ == "__main__":
    tripleStep(9)