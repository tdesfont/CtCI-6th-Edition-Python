from numpy import random

class Card:

	def __init__(self, family, value):
		self.family = family
		self.value = value

	def __str__(self):
		if self.value == 1:
			value_desc = "As"
		elif self.value <= 10:
			value_desc = str(self.value)
		else:
			value_dict = {11:"Valet", 12:"Reine", 13:"Roi"}
			value_desc = value_dict[self.value]
		family_dict = {1:"Pique", 2:"Coeur", 3:"Trefle", 4:"Carreau"}
		family_desc = family_dict[self.family]
		return "{} de {}".format(value_desc, family_desc)

class Deck:

	def __init__(self):
		print('Creation of a new deck of cards')
		self.pile = self.createFullSet()

	def pop(self):
		if not self.pile:
			print('The pile is empty...')
			return None
		else:
			return self.pile.pop()

	def createFullSet(self):
		self.pile = []
		for fam in range(1, 5):
			for value in range(0, 13):
				self.pile.append(Card(fam, value))
		return self.pile

	def shuffle(self):
		random.shuffle(self.pile)


class Player:

	def __init__(self, name):
		self.name = name
		self.hand = set()

	def receiveCard(self, card):
		self.hand.add(card)

	def removeCard(self, card):
		self.hand.discard(card)
		return card


if __name__ == '__main__':
	alice = Player("alice")
	bob = Player("bob")
	deck = Deck()
	deck.shuffle()
	for i in range(2):
		alice.receiveCard(deck.pop())
		bob.receiveCard(deck.pop())
	for card in alice.hand:
		print(card)