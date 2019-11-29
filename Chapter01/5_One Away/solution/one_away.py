"""
    One Away
"""

def oneEditAway(first, second):
    if len(first) == len(second):
        return oneEditReplace(first, second)
    elif len(first) + 1 == len(second):
        return oneEditInsert(first, second)
    elif len(first) -1 == len(second):
        return oneEditInsert(second, first)
    return False

def oneEditReplace(s1, s2):
    foundDifference = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if foundDifference:
                return False
            foundDifference = True
    return True

def oneEditInsert(s1, s2):
    """
    Check the edition operation insertion
    :param s1:
    :param s2:
    :return:
    """
    index1 = 0
    index2 = 0
    while index2 < len(s2) and index1 < len(s1):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

if __name__ == "__main__":
    assert oneEditAway("tuple", "tple")

