#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = '\n\n'
completed = True
raw_data = None # Not To be touched

def part1(data):
	fresh_ranges = data[0].split('\n')
	fresh_ranges = [[int(r) for r in x.split('-')] for x in fresh_ranges]
	ingredient_ids = [int(ing_id) for ing_id in data[1].split('\n')]
	
	return sum(any(r[0] <= ing_id <= r[1] for r in fresh_ranges) for ing_id in ingredient_ids)

def part2(data):
	fresh_ranges = data[0].split('\n')
	fresh_ranges = [[int(r) for r in x.split('-')] for x in fresh_ranges]

	evolved = True
	new_ranges = []
	while evolved:
		# print(fresh_ranges)
		for r1l, r1h in fresh_ranges:
			for i in range(len(new_ranges)):
				r2l, r2h = new_ranges[i]
				# Check for intersection...
				if (r1l <= r2l <= r1h) or (r1l <= r2h <= r1h) or (r2l <= r1l <= r2h) or (r2l <= r1h <= r2h):
					new_ranges[i] = [min(r1l, r2l), max(r1h, r2h)]
					break
			else:
				new_ranges.append([r1l, r1h])

		evolved = len(new_ranges) != len(fresh_ranges)
		fresh_ranges = new_ranges
		new_ranges = []
	
	# # We can run an assertation check...
	# for i1 in range(len(fresh_ranges)):
	# 	for i2 in range(i1 + 1, len(fresh_ranges)):
	# 		r1l, r1h = fresh_ranges[i1]
	# 		r2l, r2h = fresh_ranges[i2]
	# 		assert not ((r1l <= r2l <= r1h) or (r1l <= r2h <= r1h)), f"{fresh_ranges[i1]}, {fresh_ranges[i2]}"

	return sum((r[1] + 1 - r[0]) for r in fresh_ranges)