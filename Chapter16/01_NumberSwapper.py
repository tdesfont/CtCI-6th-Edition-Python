"""
    16.01 Number swapper
"""

def swap(a, b):
    print("a:{}, b:{}".format(a, b))
    b = a^b
    a = a^b
    b = a^b
    print("a:{}, b:{}".format(a, b))

if __name__ == "__main__":
    swap(5, 8)