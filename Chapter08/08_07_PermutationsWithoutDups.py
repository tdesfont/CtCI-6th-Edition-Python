"""
    Complexity: O(n!)
"""

permutations = []

def getPerms(base, remaining):
    """
        Get all permutations of a string.
        This string must have unique characters.
    :param string:
    :return:
    """
    n = len(remaining)
    if n == 1:
        permutations.append(base + remaining[0])
    else:
        for i in range(n):
            getPerms(base+remaining[i], remaining[:i]+remaining[i+1:])

if __name__ == "__main__":
    getPerms("", "abcde")
    print(len(permutations), permutations)