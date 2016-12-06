def random():
	"""Get the next random number in the range [0.0, 1.0)."""
	
	import time
	a = int(time.time() * 256) # use fractional seconds

	if not isinstance(a, (int, int)):
		a = hash(a)

	a, x = divmod(a, 30268)
	a, y = divmod(a, 30306)
	a, z = divmod(a, 30322)

	seed = int(x)+1, int(y)+1, int(z)+1

	# This part is thread-unsafe:
	# BEGIN CRITICAL SECTION
	
	x, y, z = seed
	x = (171 * x) % 30269
	y = (172 * y) % 30307
	z = (170 * z) % 30323
	seed = x, y, z
	# END CRITICAL SECTION

	# Note:  on a platform using IEEE-754 double arithmetic, this can
	# never return 0.0 (asserted by Tim; proof too long for a comment).
	return (x/30269.0 + y/30307.0 + z/30323.0) % 1.0
	
	
print(random())