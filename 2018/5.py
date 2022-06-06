#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = False
completed = True
raw_data = None # Not To be touched

small_alpha = 'abcdefghijklmnopqrstuvwxyz'
capti_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def react(compound:str) -> str:
	lookfor = {a:b for a, b in zip(small_alpha + capti_alpha, capti_alpha + small_alpha)}

	i = 0
	while i < len(compound) - 1: # The -1 prevents us from checking the last character
		# Check if the current two characters are what we are looking for
		if compound[i+1] == lookfor[compound[i]]:
			# If so, remove them
			compound = compound[:i] + compound[i+2:]
			continue
		i += 1
	return compound

def part1(data:str) -> int:
	# We keep reacting the compound till if cannot react anymore
	compound = data
	while True:
		reacted = react(compound)
		if len(compound) == len(reacted):
			return len(compound)
		compound = reacted

def part2(data:str) -> int:
	# In this we will take advantage of the function part1 to get the smallest possible polymer
	best_score = len(data)
	for a, b in zip(small_alpha, capti_alpha):
		# We will remove the letter a and b from the compound
		compound = data.replace(a, '').replace(b, '')
		# We react the compound entirely
		score = part1(compound)
		# Now we compare the score
		if score < best_score:
			best_score = score
	return best_score