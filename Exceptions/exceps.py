# Run this code first
try:
	fh = open('stuff.txt')
	print(fh.read())
	
	a = 1
	b = '3'
	#c = a + b # will error
	
# Catch an IO Error
except IOError:
	print('Error! Can\'t find file')

# Catch all other errors
except Exception as e:
	print(e)

# Do something if the code in 'try' worked
else:
	print('It worked!')

# Always end with this code
finally:
	print('we got to the end!')