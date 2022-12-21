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
	maxOutput = -1
	for combination in permutations(range(5, 10)):
		# Creating the 5 programs with their custom input
		programs = [computer4.from_instructions(data) for _ in range(5)]
		for i in range(5): programs[i].input(combination[i])

		previous_output = 0
		while all(not program.halted for program in programs):
			for program in programs:
				program.input(previous_output)
				output = program.run_till_output()
				if not program.halted:
					previous_output = output
		maxOutput = max(maxOutput, previous_output)



	return maxOutput