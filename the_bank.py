class BankAccount(object):
	
	def __init__(self, person_name, opening_balance = 0):
		self.balance = opening_balance
		self.name = person_name
		print("New account created for: {}".format(self.name))

	@staticmethod
	def bank_name():
		return "Nationwide"

	# Withdrawn method
	def withdraw(self, amount):
		if amount > self.balance:
			print("Sorry, insufficient funds available. You have: £{}".format(self.balance))
		else:
			self.balance -= amount
			print("£{} has been withdrawn. New balance: £{}".format(amount, self.balance))
			
	def deposit(self, amount):
		self.balance += amount
		print("£{} has been deposited. New balance: £{}".format(amount, self.balance))
		
	def transaction(self, amount, withdraw, other_account):
		if withdraw:
			self.withdraw(amount)
			other_account.deposit(amount)
		else:
			other_account.withdraw(amount)
			self.deposit(amount)


# code
a = BankAccount("Joe Bloggs", 50)
b = BankAccount("Jacob Smirthwiat", 47)
# account a gives £10 to account b
a.transaction(10, True, b)



	
	