#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = ','
completed = True
raw_data = None # Not To be touched

def part1(data):
	# You can solve this part using desmos! :)
	# https://www.desmos.com/calculator/mvmtqinhon

	data = [int(x) for x in data]
	lowest_consumption = 9e100
	for alignment in range(min(data), max(data)+1):
		# Trying out all the alignment
		fuel = 0
		for ship in data:
			fuel += abs(alignment - ship)
		lowest_consumption = min(lowest_consumption, fuel)
	return lowest_consumption

def part2(data):
	# Again this part can also be solved using desmos! :)
	# https://www.desmos.com/calculator/hmkizno1yf

	data = [int(x) for x in data]
	lowest_consumption = 9e100
	for alignment in range(min(data), max(data)+1):
		# Trying out all the alignment
		fuel = 0
		for ship in data:
			fuel += sum(range(abs(alignment - ship)+1))
		lowest_consumption = min(lowest_consumption, fuel)
	return lowest_consumption