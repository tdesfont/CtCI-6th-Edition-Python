"""
    One Away Personal Implementation
"""
def oneAway(w1, w2, i=0, j=0, d=0):
    if d > 1:
        return False
    if i > len(w1) or j > len(w2):
        return False
    if i == len(w1) and j == len(w2) and d <= 1:
        return True
    if w1[i] != w2[i]:
        d+=1
    return oneAway(w1, w2, i+1, j, d) or oneAway(w1, w2, i, j+1, d) or oneAway(w1, w2, i+1, j+1, d)

if __name__ == "__main__":
    assert oneAway("pale", "ple")
    assert not oneAway("pale", "bale")

