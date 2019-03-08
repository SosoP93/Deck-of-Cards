import unittest
from deck_of_cards import Deck

class DeckTests(unittest.TestCase):
	def setUp(self):
		self.my_deck = Deck()

	def test_count(self):
		""" Should return number of cards in the deck"""
		self.assertEqual(self.my_deck.count(), 
			52)

	def test_shuffle(self):
		""" Cards in deck should be mixed up after shuffle"""
		temp = self.my_deck.cards[:]
		self.my_deck.shuffle()	
		self.assertNotEqual(self.my_deck.cards, temp)

	def test_deal_hand(self):
		""" Number of cards in deck should reflect number of cards dealt"""
		self.my_deck.deal_hand(5)
		self.assertEqual(self.my_deck.count(), 47)

	def test_deal_card(self):
		""" Deck count should only decrease by one"""
		self.my_deck.deal_card()
		self.assertEqual(self.my_deck.count(), 51)


if __name__ == "__main__":
	unittest.main()