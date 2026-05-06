#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import combinations

def parse(data):
	lines = []
	for line in data.strip().split('\n'):
		output = line.split()
		length = len(output[0]) - 2
		target = int(output[0][1:-1].replace('#', '1').replace('.', '0'),2)
		joltage = [int(x) for x in output[-1][1:-1].split(',')]
		buttons = output[1:-1]
		nButtons = []
		for button in buttons:
			x = 0
			for i in button[1:-1].split(','):
				x |= (1 << (length - int(i) - 1))
			nButtons.append(x)

		lines.append([length, target, nButtons, joltage])
	
	return lines

split_data = parse
completed = 1
raw_data = None # Not To be touched


def part1(data):
	# This particular problem is awfully like a XOR subset finding problem.
	# We are going to take advantage of this fact to optimize the code and find the answers fast
	total = 0
	for line in data:
		length, target, nButtons, _ = line
		for i in range(1, length):
			# Now we get the subset of that length
			for comb in combinations(nButtons, r=i):
				# Now we XOR all of them.
				res = 0
				for num in comb:
					res ^= num
				if res == target:
					break
			else:
				continue
			total += i
			break

	return total
				

def part2(data):
	# This is a simple row reduction problem. Then a subspace exploration
	...
	