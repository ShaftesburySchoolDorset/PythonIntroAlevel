'''
OOP: Inheritance, overwriting, class attributes and new Object methods
'''

class Person:
		
	def __init__(self, first, last):
		self.firstname = first
		self.lastname = last
		
	def __str__(self):
		return "{} {}".format(self.firstname, self.lastname)

class Employee(Person):
	
	def __init__(self, first, last, staff_num):
		super().__init__(first, last)
		self.staffnumber = staff_num
			
	def __str__(self):
		return super().__str__() + ", #" + str(self.staffnumber)
		
class BusinessOwner():
	def __str__(self):
		return "BSO SM"
		
class Employer(BusinessOwner, Employee):
		
	def __init__(self, first, last, title):
		Employee.__init__(self, first, last, 0)
		self.title = title
			
	def __str__(self):
		return self.title + " " + Employee.__str__(self)

er = Employer("John", "Smith", "Mr")			
print(er)




