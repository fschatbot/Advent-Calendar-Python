#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .intcode import computer5

split_data = ','
completed = True
raw_data = None # Not To be touched

def part1(data):
	computer = computer5.from_instructions(data)
	computer.input(1)
	computer.run_till_end()
	return computer.recent_output

def part2(data):
	computer = computer5.from_instructions(data)
	computer.input(2)
	computer.run_till_end()
	return computer.recent_output