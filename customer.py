from atm_card import ATMCard

class Customer:
	def __init__(self, id, custPin=1234, custBalance=10000):
		self.id = id
		self.custPin = custPin
		self.custBalance = custBalance
	
	def check_id(self):
		return self.id
		
	def check_pin(self):
		return self.custPin
		
	def check_balance(self):
		return self.custBalance
		
	def withdraw_balance(self, nominal):
		self.custBalance -= nominal
		
	def deposit_balance(self, nominal):
		self.custBalance += nominal
