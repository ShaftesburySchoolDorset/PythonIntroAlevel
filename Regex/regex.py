import re

#string_to_search = 'joe.bloggs@aol.com'
#
#m = re.match(r'.*@.*\..*', string_to_search)
#
#if m != None:
#		print('found')
#else:
#		print('not found')
		
## alternative:
	
p = re.compile(r'.*@.*\..*')

while True:
	m = p.match(input('>'))
	if m == None:
		print('invalid email! :(\n')
	else:
		print('valid email :)\n')
		
		
