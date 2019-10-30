import numpy as np

class Suit:
    def __init__(self, v):
        self.suit_map = {0:"Club", 1:"Diamond", 2:"Heart", 3:"Spade"}
        self.value = v
    def getValue(self):
        return self.value
    def getSuitFromValue(self, value):
        return self.suit_map[value]

class Deck:
    def __init__(self, deckOfCards):
        self.cards = []
        self.dealtIndex = 0
        self.setDeckOfCards(deckOfCards)
        self.shuffle()
    def setDeckOfCards(self, deckOfCards):
        self.cards = deckOfCards
    def shuffle(self):
        np.random.shuffle(self.cards)
    def remainingCards(self):
        return len(self.cards)-self.dealtIndex
    def dealHand(self, number):
        pass
    def dealCard(self):
        if self.cards:
            return self.cards.pop()
        else:
            print("Empty deck of cards.")
            return None
        pass

class Card:
    def __init__(self, c, s):
        self.available = True
        self.faceValue = c
        self.suit = s
    def value(self):
        return self.faceValue
    def suit(self):
        return self.suit
    def isAvailable(self):
        return self.available
    def markUnavailable(self):
        self.available = False
    def markAvailable(self):
        self.available = True

class Hand:
    def __init__(self):
        self.cards = []
    def score(self):
        self.score = 0
        for card in self.cards:
            self.score += card.value()
        return self.score
    def addCard(self, card):
        self.cards.append(card)