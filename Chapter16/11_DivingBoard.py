"""
    16.11 Diving Board
"""

def generateLengths(shorter, longer, K):
    lengths = []
    for i in range(K+1):
        lengths.append(i*shorter + (K-i)*longer)
    return lengths

if __name__ == "__main__":
    print(generateLengths(3, 6, 8))