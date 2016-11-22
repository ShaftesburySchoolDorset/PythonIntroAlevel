class Bob():
	
	thing = "jerico"
	
	def __init__(self, thing):
		self.thing = thing
	
	def __str__(self):
		return Bob.thing + " " + self.thing

t1 = Bob("test1")
t2 = Bob("test2")
t2.thing = "james"

print(t1)
Bob.thing = "alan"

print(t2)
