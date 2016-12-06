try:
	fh = open('stuff.txt')
	print(fh.read())
	
	a = 1
	b = '3'
	#c = a + b
	
except IOError:
	print('Error! Can\'t find file')

except Exception as e:
	print(e)
	
else:
	print('It worked!')
	
finally:
	
	print('we got to the end!')