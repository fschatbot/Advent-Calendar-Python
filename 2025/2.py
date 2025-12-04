#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

split_data = ','
completed = True
raw_data = None # Not To be touched

def part1(data):
	total = 0
	for line in data:
		L, R = line.split('-')
		# One way to skip some checks is to see if an invalid can even come here
		if len(L) == len(R) and len(L) % 2 == 1: continue # Odd lengths cannot have invalids...
		for x in range(int(L), int(R)+1):
			y = str(x)
			if len(y) % 2 == 1 or y[:int(len(y) // 2)] != y[int(len(y) // 2):]: continue
			total += x
	return total

def part2(data):
	total = 0
	match = re.compile(r'^(\d+)\1+$')
	for line in data:
		L, R = line.split('-')
		for x in range(int(L), int(R)+1):
			if match.match(str(x)): total += x
	
	return total