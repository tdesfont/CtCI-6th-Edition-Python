"""
    Write a method to return all subsets of a set
    O(2**(n+1)-1)
"""

def getAllSets(S):
    S = list(S)
    n = len(S)
    subsets = [[] for i in range(1 << n)]
    for i in range(n):
        for j in range(1 << i):
            subsets[(1 << i)|j] = [S[i]] + subsets[j]
    return subsets

if __name__ == "__main__":
    S = set([1, 2, 3])
    print(getAllSets(S))