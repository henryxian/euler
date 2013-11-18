#!/usr/bin/env python

import timeit
rang = [r for r in range(0, 10)]
rang.reverse()
divider = [r for r in range(10, 91)]
divider.reverse()
max = 999 * 999
def lpp():
	for i in rang:
		for j in rang:
			for k in rang:
				#ijkkji = i*100000 + j*10000 + k*10000+...i*1
				#ijkkji = i*100001 + j*10010 + k*1100
				#ijkkji = 11*(9091*a + 910*b + 100*c)
				num = 9091 * i + 910 * j + 100 * k
				if num > max:
					continue
				for l in divider:
					#ijkkji = (11 * x) * y
					# 99 < 11*x <= 999
					# 9 < x <=90
					if num % l == 0 and num / l <= 999:
						return num * 11
if __name__ == '__main__':
	#print lpp()
	print timeit.timeit("print lpp()", number = 1, setup = "from __main__ import lpp")
