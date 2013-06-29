with open("names.txt") as names:
	names = names.read()
	# print names
	name = [i.strip('"') for i in names.split(",")]
	# print len(name)
	total_score = 0
	count = 1
	for j in sorted(name):
		score = 0
		total = 0
		for letter in j:
			total += (ord(letter) - 64)
		score = total * count
		total_score += score
		count += 1
	print total_score
