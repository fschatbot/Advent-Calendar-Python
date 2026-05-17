#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

split_data = False
completed = 1
raw_data = None # Not To be touched

def part1(data):
	row, col = re.search(r"To continue, please consult the code grid in the manual.  Enter the code at row (\d+), column (\d+).", data).groups()
	r, c = int(row), int(col)
	n = ((r + c - 2) * (r + c - 1)) // 2 + c

	code = 20151125
	for _ in range(1, n):
		code = (code * 252533) % 33554393
	
	return code

def part2(data):
	...