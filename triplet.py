from math import sqrt
if __name__ == '__main__':
	found = False
	for a in xrange(1, 1001):
		for b in xrange(a, 1001):
			result = a + b + sqrt(a ** 2 + b ** 2)
			if result == 1000:
				print a * b * sqrt(a ** 2 + b ** 2)
				found = True
				break
		if found:
			break