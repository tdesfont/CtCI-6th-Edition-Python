from collections import defaultdict

def isUnique(string):
    """
    Check if a string has all unique characters.
    :param string:
    :return:
    """
    if not string:
        return True
    string = string.lower()
    char_count = defaultdict(int)
    for char in string:
        assert ord('a') <= ord(char)
        assert ord(char) <= ord('z')
        if char_count[ord(char)] == 1:
            return False
        char_count[ord(char)] += 1
    return True

if __name__ == "__main__":
    print(isUnique("azerty"))