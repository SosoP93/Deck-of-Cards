from random import shuffle

class Card:

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return f"{self.value} of {self.suit}"

class Deck:

	def __init__(self):
		suits = ["Hearts", "Diamonds",  "Clubs", "Spades"]
		values = list(("A,2,3,4,5,6,7,8,9,10,J,Q,K".split(",")))
		self.cards = [Card(suit, value) for suit in suits for value in values]

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def _deal(self, num):
		removed = []
		if self.count() == 0:
			raise ValueError("All cards have been dealt")
		else : 
			while num:
				num -= 1
				removed.append(self.cards.pop(0))
			return removed
			 	
	def count(self):
		return len(self.cards)

	def shuffle(self):
		if self.count() != 52:
			raise ValueError("Only full decks can be shuffled")	
		return shuffle(self.cards)

	def deal_card(self):
		card = self._deal(1)
		return card[0]

	def deal_hand(self, hand_size):
		hand = self._deal(hand_size)
		return hand
