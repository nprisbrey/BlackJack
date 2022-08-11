from cards import *
from random import shuffle

NUM_DECKS_USED = 6
NUM_CARDS_CUT = 60
# Maximum amount of cards left in the deck at the end of the round after which the deck will
# be shuffled and reset
THRES_TO_SHUFFLE = 30

deck = []

def newDeck():
	"""Refill deck, shuffle, and cut cards"""
	
	freshDeck = [Card(suit,value) for _,value in CardValue.__members__.items() for _,suit in CardSuit.__members__.items() for _ in range(NUM_DECKS_USED)]
	
	shuffle(freshDeck)
	
	freshDeck[:NUM_CARDS_CUT] = []
	
	return freshDeck

def newRound():
	pass
	
deck = newDeck()
print(deck[0])
