#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .intcode import computer5

split_data = ','
completed = 1
raw_data = None # Not To be touched

def part1(data):
	computer = computer5.from_instructions(data)
	computer.run_till_end()
	return sum(output == 2 for output in computer.outs[2::3])

def part2(data):
	data[0] = 2
	computer = computer5.from_instructions(data)
	