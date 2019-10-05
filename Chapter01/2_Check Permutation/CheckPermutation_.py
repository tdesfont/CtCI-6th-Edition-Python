
def check_permutations(string1, string2):
    counter = dict()
    for letter in string1.lower():
        code = ord(letter)
        assert ord('a') <= code
        assert code <= ord('z')
        if code not in counter:
            counter[code] = 1
        else:
            counter[code] += 1
    print(counter)
    for letter in string2.lower():
        code = ord(letter)
        assert ord('a') <= code
        assert code <= ord('z')
        if code not in counter:
            return False
        else:
            counter[code] -= 1
    print(counter)
    for code in counter:
        if abs(counter[code]) > 0:
            return False
    return True

if __name__ == "__main__":
    print(check_permutations('aec', 'cae'))
