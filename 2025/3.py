#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	total = 0
	for bank in data:
		battery = [int(joltage) for joltage in bank]

		# Find the largest first unit that is the most left...
		max_f = -1
		max_i = -1
		for i, j in enumerate(battery[:-1]):
			if j > max_f:
				max_i, max_f = i, j
		# Next find the second largest on the right hand side and we are done
		total += max_f * 10 + max(battery[max_i+1:])
	
	return total

def argmax(array:list) -> int:
	best = -1
	best_i = -1

	for i, j in enumerate(array):
		if j > best:
			best_i, best = i, j

	return best_i


def part2(data):
	# Same logic as above, simply extended

	total = 0
	for bank in data:
		bank = [int(joltage) for joltage in bank]
		digits = 11 # extra digits remaining
		i = -1
		final_joltage = 0
		while digits >= 0:
			num = argmax(bank[i+1:-digits] if digits != 0 else bank[i+1:])
			i += num+1
			final_joltage = final_joltage * 10 + bank[i]
			digits -= 1
		total += final_joltage
	
	return total