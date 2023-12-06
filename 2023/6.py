#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	timings = [int(x) for x in re.findall(r'\d+', data[0])]
	records = [int(x) for x in re.findall(r'\d+', data[1])]

	acc = 1
	for limit, record in zip(timings, records):
		# First we find the first instance we won:
		for pushFor in range(limit):
			if (limit - pushFor) * pushFor > record:
				acc *= limit - 2 * pushFor + 1 # MaxSec - MinSec + 1 -> (limit - pushFor) - pushFor + 1 -> limit - 2 * pushFor + 1
				break
	return acc

def part2(data):
	limit = int(data[0].replace(' ','').split(':')[1])
	record = int(data[1].replace(' ','').split(':')[1])

	for pushFor in range(limit):
		if (limit - pushFor) * pushFor > record:
			return limit - 2 * pushFor + 1 # Same Logic