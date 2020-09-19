class ATMCard:
	def __init__(self, defaultPin, defaultBalance):
		self.defaultPin = defaultPin
		self.defaultBalance = defaultBalance
	
	def cek_pin_awal(self):
		return self.defaultPin
		
	def cek_saldo_awal(self):
		return self.defaultBalance
