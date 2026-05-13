#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	total = 0
	for initial in data:
		secret = int(initial)
		for _ in range(2000):
			secret = ((secret * 64) ^ secret) % 16777216
			secret = ((secret // 32) ^ secret) % 16777216
			secret = ((secret * 2048) ^ secret) % 16777216
		total += secret
	
	return total

def part2(data):
	sequence = {}
	for initial in data:
		secret = int(initial)
		prev5, prev4, prev3, prev2, prev1 = None, None, None, None, secret % 10
		monkey_sequence = set()
		for _ in range(2000):
			secret = ((secret * 64) ^ secret) % 16777216
			secret = ((secret // 32) ^ secret) % 16777216
			secret = ((secret * 2048) ^ secret) % 16777216
			prev5, prev4, prev3, prev2, prev1 = prev4, prev3, prev2, prev1, secret % 10
			if prev5 is not None:
				# We can now calculate the previous four sequence:
				seq = f"{prev4-prev5},{prev3-prev4},{prev2-prev3},{prev1-prev2}"
				if seq not in monkey_sequence: sequence[seq] = sequence.get(seq, 0) + prev1
				monkey_sequence.add(seq)
	
	return max(sequence.values())