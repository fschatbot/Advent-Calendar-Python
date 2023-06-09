#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = ','
completed = True
raw_data = None # Not To be touched

def part1(data):
	laterns = [int(x) for x in data]
	for _ in range(80):
		# print(', '.join(str(x) for x in laterns))
		new_laterns = []
		for fish in laterns:
			next_timer = fish-1
			if next_timer < 0:
				new_laterns.extend([6, 8])
			else:
				new_laterns.append(next_timer)
		
		laterns = new_laterns
	
	return len(laterns)

def part2(data):
	# Had this epiphany of using frequencies to do mass calculation when 
	# I was thinking of grouping all the new_borns in an array to do mass calculations. Heh!
	frequency = {x: 0 for x in range(9)}
	for x in data: frequency[int(x)] += 1 # Parsing

	for _ in range(256):
		new_frequency = {x: 0 for x in range(-1, 9)}
		for key, value in frequency.items(): new_frequency[key-1] = value # Reducing the timer for all fishes
		
		new_frequency[8] = new_frequency[-1] # Add the offsprings
		new_frequency[6] += new_frequency[-1] # Reset their cycle
		del new_frequency[-1] # As we reset their cycle there is no one in -1 category

		frequency = new_frequency
	
	return sum(frequency.values())