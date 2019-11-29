"""
    1.6 String Compression
"""

def compress_recursive(string):
    """
    Recursive approach for the string compression
    :param string:
    :return:
    """
    if not string:
        return ""
    i = 0
    count = 1
    while i < len(string)-1 and string[i] == string[i+1]:
        count += 1
        i += 1
    return string[i]+str(count)+compress_recursive(string[i+1:])

def compress_helper(string):
    compressed_string = compress_recursive(string)
    if len(compressed_string) < len(string):
        return compressed_string
    else:
        return string

def compress_iterative(string):
    """
    Iterative approach for the solution
    :param string:
    :return:
    """
    if len(string) < 2:
        return string
    assert "#" not in string
    string += "#"
    count_list = []
    rep = string[0]
    count = 1
    for i in range(0, len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            count_list.append((rep, count))
            count = 1
            rep = string[i+1]
    new_string = "".join([rep+str(count) for rep, count in count_list])
    return new_string


if __name__ == "__main__":
    print(compress_recursive("aabbbcccc"))
    assert compress_recursive("aabbbcccc") == "a2b3c4"
    print(compress_helper("abc"))
    print(compress_iterative("aabbcccccc"))