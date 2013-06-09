from math import sqrt
def max_prime_factor(num):
	for i in range(2, int(sqrt(num)) + 1):
		if num % i == 0:
			return max_prime_factor(num / i)
	return num
if __name__ == '__main__':
	print max_prime_factor(600851475143)