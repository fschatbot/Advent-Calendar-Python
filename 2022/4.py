#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	counter = 0
	for pair in data:
		# Parsing the line into indivual variables
		elf1, elf2 = pair.split(',')
		e1_lower, e1_higher = elf1.split('-')
		e2_lower, e2_higher = elf2.split('-')
		# Converting the extracted numbers into ints
		e1_lower, e1_higher, e2_lower, e2_higher = int(e1_lower), int(e1_higher), int(e2_lower), int(e2_higher)
		# Using ifs to check wheter an elf range falls under the other elf
		if e1_lower <= e2_lower and e1_higher >= e2_higher: # Checking for elf 2 overlapped by elf 1
			counter += 1
		elif e2_lower <= e1_lower and e2_higher >= e1_higher: # Checking for elf 1 overlapped by elf 2
			counter += 1
	return counter

def part2(data):
	counter = 0
	for pair in data:
		# Parsing the line into indivual variables
		elf1, elf2 = pair.split(',')
		e1_lower, e1_higher = elf1.split('-')
		e2_lower, e2_higher = elf2.split('-')
		# Converting the extracted numbers into ints
		e1_lower, e1_higher, e2_lower, e2_higher = int(e1_lower), int(e1_higher), int(e2_lower), int(e2_higher)
		# If the other elf number is between the others range, then it is overlapping
		if e1_lower <= e2_lower <= e1_higher or e1_lower <= e2_higher <= e1_higher:
			counter += 1
		elif e2_lower <= e1_lower <= e2_higher or e2_lower <= e1_higher <= e2_higher:
			counter += 1
	return counter