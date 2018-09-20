def gcd(a, b):
	"""
	Greatest Common Divisor
	take advantages of bit manipulation
	"""
	if b:
		a_is_odd = a%2
		b_is_odd = b%2
		if a_is_odd and b_is_odd:
			return gcd(b, a%b)
		elif a_is_odd:
			return gcd(a, b>>2)
		elif b_is_odd:
			return gcd(a>>2, b)
		return gcd(a>>2, b>>2) << 2
	else :
		return a

def lcm(a, b):
	"""
	Least common multiplier
	"""
	return a*b//gcd(a,b)