"""
    Similar to the HashMapList written in Java, we would like to create a data structure that allows
    the following operations:
        d = hashMap()  # Creation
        d['apple'] = 1 # Key Value assignment
        del d['apple'] # Key Value deletion
    Warnings:
        key collision
        hash function
"""

from collections import defaultdict

d = dict()
d['apple'] = 1
d['banana'] = 2
del d['apple']


def compute_hash_value(key):
    """
    Compute hash code of a key to select the index of the
    :param key: <str> String
    :return:
    """
    sum = 0
    for letter in key:
        sum += ord(letter)
    return sum


class HashMapList:

    def __init__(self):
        self.map = dict()

    def put_item(self, key, item):
        """
        :param key:
        :param item: <str>
        :return:
        """
        if key not in self.map:
            self.map[key] = []
        self.map[key].append(item)

    def put_list(self, key, items):
        """
        :param key:
        :param items: <list[str]>
        :return:
        """
        for item in items:
            self.put_item(key, item)

    def get(self, key):
        return map[key]

    def contains_key(self, key):
        return key in self.map

    def contains_key_value(self, key, value):
        # Could have been: return value in self.map[key]
        items_list = self.map[key]
        if not items_list:
            return False
        return value in items_list

    def key_set(self):
        return set(self.map.keys())

    def __str__(self):
        pprint_string = ""
        for key in self.map:
            pprint_string += str(key)
            pprint_string += "\n"
            for value in self.map[key]:
                pprint_string += str(value) + "->"
            pprint_string += "None\n\n"
        return pprint_string

if __name__== "__main__":
    hashMapList = HashMapList()
    hashMapList.put_list('apple', [2, 4, 6])
    hashMapList.put_list('banana', [1, 3, 5])
    print(hashMapList.key_set())
    print(hashMapList)
    print(hashMapList.contains_key('apple'))