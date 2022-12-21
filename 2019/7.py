#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import permutations
from .intcode import computer4

split_data = ','
completed = 1
raw_data = None # Not To be touched

def part1(data):
	maxOutput = -1
	for combination in permutations(range(5), 5):
		# Testing out the combination
		output = 0
		for phase in combination:
			computer = computer4.from_instructions(data)
			computer.input(phase, output)
			output = computer.run_till_output()
		
		maxOutput = max(maxOutput, output)
	return maxOutput

def part2(data):
	...