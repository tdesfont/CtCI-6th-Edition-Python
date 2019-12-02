"""
    Chapter 8: Recursion and Dynamic Programming
    Question 1: Triple Step
"""

def count_ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return count_ways(n-1)+count_ways(n-2)+count_ways(n-3)

if __name__ == "__main__":
    for i in range(10):
        print(count_ways(i))