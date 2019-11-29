"""
    One Away Personal Implementation
"""

def one_away(w1, w2):
    n = len(w1)
    m = len(w2)
    A = [[i+j for j in range(m+1)] for i in range(n+1)] # The value does not matter
    for i in range(n):
        for j in range(m):
            A[i+1][j+1] = min(A[i][j+1]+1,
                              A[i+1][j]+1,
                              A[i][j]+int(w1[i]!=w2[j]))
    return A[n][m] == 1

if __name__ == "__main__":
    assert one_away("pale", "ple")
    assert one_away("pale", "bale")
