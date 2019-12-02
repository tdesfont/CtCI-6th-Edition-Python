"""
    Chapter 8: Recursion and Dynamic Programming
    Question 4: Power Set
"""

import time

def subsets(s):
    """
    Compute all the subsets using a naive approach of time complexity O(n.2^n)
    :param s:
    :return:
    """
    try:
        assert type(s) is set
    except:
        s = set(s)
    s = list(s)
    n = len(s)
    S = []
    for i in range(2**n):
        subset = set()
        for j in range(n):
            if i & 1<<j:
                subset.add(s[j])
        S.append(subset)
    return S

def subsets_memo(s):
    """
    Reduce to time complexity of O(2^n) by using memoization
    :param s:
    :return:
    """
    try:
        assert type(s) is set
    except:
        s = set(s)
    n = len(s)
    s = list(s)
    S = [set() for i in range(2**n)]
    for i in range(n):
        for j in range(1<<i):
            S[1 << i | j] = S[j].copy() # do not forget the .copy()
            S[1 << i | j].add(s[i])
    return S

if __name__ == "__main__":

    N = 15
    print(N)
    s = set(list(range(N)))

    t0 = time.time()
    subsets_memo(s)
    t0 = time.time() - t0

    t1 = time.time()
    subsets(s)
    t1 = time.time() - t1

    print(t0, t1)
