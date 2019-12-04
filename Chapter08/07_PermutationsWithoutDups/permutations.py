"""
    Chapter 8: Recursion and Dynamic Programming
    Question 7: Permutations without Dups
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def get_permutations(string):
    permutation_list = []
    def permutations(string="", remaining_set=set()):
        if not remaining_set:
            permutation_list.append(string)
        else:
            for letter in remaining_set:
                permutations(string+letter, remaining_set-set([letter]))
    permutations("", remaining_set=set(string))
    assert len(permutation_list) == factorial(len(string))
    return permutation_list

if __name__ == "__main__":
    print(get_permutations("abcde"))