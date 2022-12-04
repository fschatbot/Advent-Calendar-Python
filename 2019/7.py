#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import permutations
from .intcode import computer4

split_data = ','
completed = False
raw_data = None # Not To be touched

def part1(data):
	maxOutput = -1
	for combination in permutations(range(5), 5):
		# Testing out the combination
		output = 0
		for phase in combination:
			outputs = computer4(data.copy(), [phase, output])
			output = outputs[0]
		
		maxOutput = max(maxOutput, output)
	return maxOutput

def part2(data):
	...