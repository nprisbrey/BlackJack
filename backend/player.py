class Player():
	def __init__(self, websocket):
		self.wsock = websocket
		self.money = 0
		self.name = None
	
	def __str__(self):
		return f"{self.name}, ${self.money}"
	
	def getMoney(self):
		return self.money
	
	def getName(self):
		return self.name
	
	def gainMoney(self, amount):
		self.money += amount
	
	def loseMoney(self, amount):
		"""Decrease self.money. Don't go below 0"""
		self.money -= min(self.money, amount)
	
	def setMoney(self, amount):
		self.money = amount
	
	def setName(self, name):
		self.name = name
