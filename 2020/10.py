#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	data = sorted(int(x) for x in data)
	data.append(data[-1]+3)
	
	diff = [0, 0, 0]
	prev_adp = 0
	for adapter in data:
		diff[adapter - prev_adp - 1] += 1
		prev_adp = adapter

	return diff[0] * diff[2]

def part2(data):
	# This code only works because:
	# There is no adapter difference of 2
	# The maximum streak of ones seen is 4
	# The multipliers were manually calculated by sitting down and doing it on paper.
	# More efficient methods exists such as recursion checking using memoization...


	

	streak_mult = [1, 1, 2, 4, 7]
	data = sorted(int(x) for x in data)
	data.append(data[-1]+3)
	
	total_comb = 1
	prev_adp = 0
	one_streak = 0
	for adapter in data:
		if adapter - prev_adp == 1:
			one_streak += 1
		else:
			total_comb *= streak_mult[one_streak]
			one_streak = 0
		prev_adp = adapter

	return total_comb


	# The following is a recurive solution from reddit megathread that is more neat and clean
	from functools import cache

	data.insert(0, 0)

	@cache
	def recursive_sol(rating):
		if rating == 0: return 1 # Only count if we were able to reach all the way down...
		options = [opt for opt in range(rating-3, rating) if opt in data]
		return sum(recursive_sol(opt) for opt in options)
	
	return recursive_sol(data[-1])
