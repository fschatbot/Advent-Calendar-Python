#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = int
completed = True
raw_data = None # Not To be touched

def part1(data):
	buffer = [0]
	pos = 0
	for i in range(2017):
		pos = (pos + data) % len(buffer) + 1
		buffer.insert(pos, i + 1)
	return buffer[pos + 1]

def part2(data):
	# Instead of making a buffer we keep track of zero
	# If something is added before it we push zero's index one step forward
	# If something is added right after zero we keep track of it!

	zeroIndex = 0
	afterZero = None
	pos = 0
	for i in range(50_000_000):
		pos = (pos + data) % (i+1) + 1 # The position this number will be inserted to!

		if pos <= zeroIndex: zeroIndex += 1
		elif zeroIndex+1 == pos: afterZero = i+1
	
	return afterZero