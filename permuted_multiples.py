#!/usr/bin/env python

def func(seq):
	seq = str(seq)
	collection = set()
	for i in seq:
		collection.add(i)
	return collection

num = 1
while True:
	if func(num) == func(2 * num) == func(3 * num) == func(4 * num) == func(5 * num) == func(6 * num):
		break
	num += 1
print num