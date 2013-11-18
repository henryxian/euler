#!/usr/bin/env python

def even(num):
	if num < 2:
		return "no even-valued term found"
	elif num >= 2 and num < 8:
		return 2
	elif num == 8:
		return 10
	else:
		even1 = 2
		even2 = 8
		total = 10
		while even2 <= num:
			#every third term in Fibonacci is even.
			even1, even2 = even2, even2 * 4 + even1
			if even2 <= num:
			#add up the terms not exceed the limit num.
				total += even2
		return total
if __name__ == '__main__':
	print even(34)