"""
    Chapter 3, Question 6: Animal Shelter
"""

from collections import deque

class Animal:

    def __init__(self, name, type):
        self.name = name
        self.type = type
        assert self.type == "dog" or self.type == "cat"

class AnimalShelter:

    def __init__(self):
        self.cat_queue = deque()
        self.dog_queue = deque()
        self.time = 0

    def enqueue(self, animal):
        self.time += 1
        if animal.type == "cat":
            self.cat_queue.appendleft((animal, self.time))
        else:
            self.dog_queue.appendleft((animal, self.time))

    def dequeue(self):
        if not self.cat_queue and not self.dog_queue:
            return None
        elif not self.cat_queue:
            return self.dog_queue.pop()[0].name
        elif not self.dog_queue:
            return self.cat_queue.pop()[0].name
        else:
            last_dog = self.dog_queue.pop()
            last_cat = self.cat_queue.pop()
            if last_dog[1] < last_cat[1]:
                # must deque dog
                self.cat_queue.append(last_cat)
                return last_dog[0].name
            else:
                self.dog_queue.append(last_dog)
                return last_cat[0].name

    def dequeue_dog(self):
        if not self.dog_queue:
            return None
        else:
            return self.dog_queue.pop()[0].name

    def dequeue_cat(self):
        if not self.cat_queue:
            return None
        else:
            return self.cat_queue.pop()[0].name

if __name__ == "__main__":
    animals = [
        Animal("Bruce", "dog"),
        Animal("Rex", "dog"),
        Animal("Feedo", "cat"),
        Animal("Smith", "cat"),
               ]
    shelter = AnimalShelter()
    for animal in animals:
        shelter.enqueue(animal)
    print(shelter.dequeue_cat())
    print(shelter.dequeue())
    print(shelter.dequeue_dog())
    print(shelter.dequeue_cat())
    print(shelter.dequeue())

