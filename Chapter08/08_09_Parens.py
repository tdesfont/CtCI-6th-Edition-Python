def generateParens(remaining):
    S = set()
    if remaining == 0:
        S.add("")
    else:
        prev = generateParens(remaining-1)
        for string in prev:
            for i in range(0, len(string)):
                if string[i] == "(":
                    s = insertInside(string, i)
                    S.add(s)
            S.add("()"+string)
    return S

def insertInside(string, leftIndex):
    left = string[0:leftIndex+1]
    right = string[leftIndex+1: len(string)]
    return left + "()" + right

if __name__ == "__main__":
    print(generateParens(3))