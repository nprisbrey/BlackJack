from enum import Enum, auto

class CardSuit(Enum):
	CLUBS = auto()
	HEARTS = auto()
	DIAMONDS = auto()
	SPADES = auto()

class CardValue(Enum):
	ACE = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SIX = 6
	SEVEN = 7
	EIGHT = 8
	NINE = 9
	TEN = 10
	JACK = 10
	QUEEN = 10
	KING = 10

class Card():
	def __init__(self,suit,value):
		self.suit = suit
		self.value = value
	
	def __str__(self):
		return f"{self.value._name_} of {self.suit._name_}"
	
	def getSuit():
		return self.suit
	
	def getValue():
		return self.value
