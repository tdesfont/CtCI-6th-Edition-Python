"""
    Write a method to return all subsets of a set
    O(n.2**n)
"""

def getAllSets(S):
    S = list(S)
    n = len(S)
    subsets = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(S[j])
        subsets.append(subset)
    assert len(subsets) == 2**n
    return subsets

if __name__ == "__main__":
    S = set([1, 2, 3])
    print(getAllSets(S))