#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(data):
	new_data = []
	for line in data.split('\n'):
		depth, Drange = line.split(': ')
		new_data.append((int(depth), int(Drange)))
	return new_data

split_data = parse
completed = True
raw_data = None # Not To be touched

def part1(data):
	acc = 0
	for depth, Drange in data:
		# Overhere we simiulate the scanner at each depth and check for collision
		at = 0
		goUp = True
		for _ in range(depth):
			at += 1 if goUp else -1
			if not (0 <= at < Drange):
				goUp = not goUp
				at += 2 if goUp else -2
		if at == 0: acc += depth * Drange
	return acc		

def part2(data):
	delay = 0
	while True:
		for depth, Drange in data:
			# Instead of simulating it, we quickly calculate it!
			moves = depth + delay
			# Each cycle lasts for 2 * Drange - 2
			remaingingMoves = moves % (2 * Drange - 2)

			# If more than the Drange then we know that the scanner is comming backwards
			# Else we know the scanner is in normal position
			if remaingingMoves >= Drange:
				at = 2 * Drange - remaingingMoves
			else:
				at = remaingingMoves
			
			# Check if we got caught, we stop checking
			if at == 0:
				break
		else:
			return delay # This will only run if the for loop never breaks
		delay += 1