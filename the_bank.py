class BankAccount(object):
	
	def __init__(self, person_name, opening_balance = 0):
		self.__balance = opening_balance
		self.name = person_name
		print("New account created for: {}".format(self.name))

	@staticmethod
	def bank_name():
		return "Nationwide"

	# Withdrawn method
	def withdraw(self, amount):
		if amount > self.__balance:
			print("Sorry, insufficient funds available. You have: £{}".format(self.__balance))
		else:
			self.__balance -= amount
			print("£{} has been withdrawn. New __balance: £{}".format(amount, self.__balance))
			
	def deposit(self, amount):
		self.__balance += amount
		print("£{} has been deposited. New __balance: £{}".format(amount, self.__balance))
		
	def transaction(self, amount, withdraw, other_account):
		if withdraw:
			self.withdraw(amount)
			other_account.deposit(amount)
		else:
			other_account.withdraw(amount)
			self.deposit(amount)


# code
a = BankAccount("Joe Bloggs", 50)
print(a.__balance)
a.__balance -= 150
print(a.__balance)



	
	