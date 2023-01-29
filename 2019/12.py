#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from itertools import permutations, combinations
from math import lcm

def process_data(data):
	moon_scans = data.split('\n')
	regex = re.compile(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>')
	moons = []
	for moon_scan in moon_scans:
		m = regex.match(moon_scan)
		position = [int(point) for point in m.groups()]
		moons.append({
			'pos': position, # position
			'vel': [0, 0, 0] # velocity
		})
	return moons

split_data = process_data
completed = True
raw_data = None # Not To be touched

def part1(data):
	moons = data.copy()
	for _ in range(1000):
		# Looping through all the possible pairs
		# For a faster method we can use combination instead permutation and update the velocity of both the moons at the same time
		# However, this method is slightly simpler and hence used
		for moon1, moon2 in permutations(moons, 2):
			# Updating the moon1's velocity by looping through each axis
			for axisIndex in range(3):
				if moon1['pos'][axisIndex] == moon2['pos'][axisIndex]: continue # skip the update if both the axis are the same
				moon1['vel'][axisIndex] += 1 if moon2['pos'][axisIndex] > moon1['pos'][axisIndex] else -1
			
		# Now that the velocity is updated, we will update the position
		for moon in moons:
			# Writing this is much simpler than a for loop
			moon['pos'][0] += moon['vel'][0]
			moon['pos'][1] += moon['vel'][1]
			moon['pos'][2] += moon['vel'][2]
		
	# Now that we calculated the final posisitions, we will calculate the total energy
	total_energy = 0
	for moon in moons:
		total_energy += sum(abs(x) for x in moon['pos']) * sum(abs(x) for x in moon['vel'])

	return total_energy

def part2(data):
	# While I could modify the above code and call it a day, it would simply take way to long and I am not willing to brute force the answer
	# If we analyze the question carefully, we will notice that each axis of the planet moves independently to each other.
	# This means that if we find the period after which each of the axis return to their initial stage.
	# We can find the LCM of those indiviual periods to get the period after which the entire system gets to its initial stage
	moons = data.copy()
	periods = [] # List of period after which each axis is back to inital stage

	def encode(position): return '|'.join(f'{x},{y}' for x, y in position) # A Simple encoder for the `axisPositions` variable

	for axisIndex in range(3):
		axisPositions = [[moon['pos'][axisIndex], 0] for moon in moons] # [[position, velocity], ...]
		inital_state = encode(axisPositions) # encoding the initial data
		counter = 0

		while counter == 0 or encode(axisPositions) != inital_state:
			counter += 1

			# Updating the velocity
			for pos1, pos2 in combinations(axisPositions, 2):
				if pos1[0] > pos2[0]:
					pos1[1] -= 1
					pos2[1] += 1
				elif pos1[0] < pos2[0]:
					pos1[1] += 1
					pos2[1] -= 1
			
			# Updating the positions
			for pos in axisPositions:
				pos[0] += pos[1]
		
		periods.append(counter)
	
	return lcm(*periods)