from bisect import bisect

def smallestDifference(array1, array2):
    """

    :param array1:
    :param array2:
    :return:
    """
    array1 = sorted(array1)
    array2 = sorted(array2)
    minimum = float('inf')
    optimalCouple = None
    for i, val in enumerate(array1):
        j = bisect(array2, val)-1 # Warning: Do not forget the -1 here
        diff = val - array2[j]
        if  0 <= diff < minimum:
            minimum = diff
            optimalCouple = (i, j)
    if optimalCouple:
        print(array1[optimalCouple[0]], array2[optimalCouple[1]])
    return optimalCouple

if __name__ == "__main__":
    array1 = [1, 3, 15, 11, 12]
    array2 = [23, 127, 235, 19, 8]
    print(smallestDifference(array1, array2))