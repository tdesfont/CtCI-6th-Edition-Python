def magicIndex(A):
    for i in range(0, len(A)):
        if A[i] == i:
            print(i, A[i])
            return True
    return False

if __name__ == "__main__":
    magicIndex([2, 4, 5, 5, 5, 5])