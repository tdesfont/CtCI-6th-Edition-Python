def getPerms(remainder):
    n = len(remainder)
    result = []
    if n == 0:
        result.append('')
        return result
    for i in range(n):
        before = remainder[0:i]
        after = remainder[i+1:]
        partials = getPerms(before+after)
        for s in partials:
            result.append(remainder[i]+s)
    return result

if __name__ == "__main__":
    print(getPerms("abcde"))