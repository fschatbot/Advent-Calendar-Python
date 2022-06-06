#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	twice = 0
	thrice = 0

	for line in data:
		# Get a list of all the characters in the line
		line_set = set(line)
		if len(line_set) == len(line): # Quick Check to make sure that there are sum duplicates
			continue
		
		# Check if any of characters appear twice or thrice
		if any(line.count(c) == 2 for c in line_set):
			twice += 1

		if any(line.count(c) == 3 for c in line_set):
			thrice += 1
	
	return twice * thrice

def part2(data):
	best_match_common_letters = ""
	best_score = len(data[0]) # Max length of a sample string

	# O(n^2) to iterate through all the possible matches
	# O(x) to find the best match (x = length of the sample strings)
	# Hence the solution is O(n^2 * x)

	for id1 in data:
		for id2 in data:
			if id1 == id2: continue
			score = 0
			match_str = ""
			for char1, char2 in zip(id1, id2):
				if char1 != char2:
					score += 1
				else:
					match_str += char1
				
				if score > best_score:
					break
			else:
				if score < best_score:
					best_score = score
					best_match_common_letters = match_str
	
	return best_match_common_letters