def collatz(num):
	count = 0
	if num == 1:
		count = 4
		return count
	while True:
		if num == 1:
			count += 1
			break
		elif num % 2 == 0:
			count += 1
			num /= 2
		else:
			count += 1
			num = 3 * num + 1
	return count

if __name__ == '__main__':
	max = 0
	for i in xrange(1, 1000000):
		col = collatz(i)
		if col > max:
			max = col
			result = i
	print max
	print result
	# print collatz()