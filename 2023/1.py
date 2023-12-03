#!/usr/bin/env python
# -*- coding: utf-8 -*-

import regex as re

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	acc = 0
	for line in data:
		digits = [char for char in line if char.isdigit()]
		acc += int(digits[0]+digits[-1])
	return acc

def part2(data):
	hashMap = {
		'one': '1',
		'two': '2',
		'three': '3',
		'four': '4',
		'five': '5',
		'six': '6',
		'seven': '7',
		'eight': '8',
		'nine': '9'
	}

	acc = 0
	for line in data:
		out = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
		first = out[0] if out[0].isdigit() else hashMap[out[0]]
		last = out[-1] if out[-1].isdigit() else hashMap[out[-1]]
		acc += int(first + last)
	
	return acc