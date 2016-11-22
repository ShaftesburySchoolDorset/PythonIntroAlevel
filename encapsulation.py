class testClass(object):
	
	def __init__(self):
		self.a = 10 # public - works fine
		self._a = 11 # private - works, but is unconvential to access outside a class
		self.__a = 12 # protected - can't be accessed outside a class
		
t = testClass()
print(t.a)
print(t._a)
print(t.__a)