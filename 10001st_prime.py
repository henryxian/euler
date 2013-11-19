#!/usr/bin/env python

from math import sqrt
if __name__ == '__main__':
	count = 0
	num = 1
	while True:
		if count == 10001:
			print num
			break
		num += 1
		print num
		print count
		if int(sqrt(num)) < 2:
			count += 1
		else:
			for i in xrange(2, int(sqrt(num)) + 1):
				if num % i == 0:
					break
			else:
				count += 1
