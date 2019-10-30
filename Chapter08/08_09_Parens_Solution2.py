def addParen(l, leftRem, rightRem, string, count):
    if leftRem < 0 or rightRem < leftRem:
        return
    if leftRem == 0 and rightRem == 0:
        s = string[::]
        l.append(s)
    else:
        if leftRem > 0:
            string[count] = '('
            addParen(l, leftRem-1, rightRem, string, count+1)
        if rightRem > leftRem:
            string[count] = ')'
            addParen(l, leftRem, rightRem-1, string, count+1)

def generateParens(count):
    string = [None]*(2*count)
    l = []
    addParen(l, count, count, string, 0)
    l = ["".join(l_) for l_ in l]
    return l

if __name__ == "__main__":
    print(generateParens(3))
