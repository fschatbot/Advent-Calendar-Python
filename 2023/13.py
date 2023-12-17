#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
import numpy as np

split_data = '\n\n'
completed = True
raw_data = None # Not To be touched

def part1(data:List[str]):
	acc = 0
	for pattern in data:
		pattern = pattern.split('\n')
		p = np.array([[1 if x == '#' else 0 for x in line] for line in pattern])
		px, py = len(pattern[0]), len(pattern)

		# Checking hortizontally
		for i in range(py):
			s = min(py - i, i)
			if np.array_equal(p[:i][::-1][:s], p[i:][:s]):
				acc += 100 * i
		
		# Checking vertically
		# Rotate the array 270deg
		p = np.rot90(p, 3)
		for i in range(px):
			s = min(px - i, i)
			if np.array_equal(p[:i][::-1][:s], p[i:][:s]):
				acc += i
	return acc


def part2(data:List[str]):
	acc = 0
	for pattern in data:
		pattern = pattern.split('\n')
		py = len(pattern)

		# Checking hortizontally
		for i in range(1, py):
			s = min(py - i, i)
			a = pattern[:i][::-1][:s]
			b = pattern[i:][:s]

			diff = 0
			for a1, b1 in zip(a, b):
				for c1, c2 in zip(a1, b1):
					if c1 != c2: diff += 1

			if diff == 1:
				acc += 100 * i
		
		# Checking vertically

		# Rotate the array 270deg
		pattern = np.array([[x for x in line] for line in pattern])
		pattern = np.rot90(pattern, 3)
		pattern = [''.join(line) for line in pattern.tolist()]

		py = len(pattern)

		for i in range(1, py):
			s = min(py - i, i)
			a = pattern[:i][::-1][:s]
			b = pattern[i:][:s]

			diff = 0
			for a1, b1 in zip(a, b):
				for c1, c2 in zip(a1, b1):
					if c1 != c2: diff += 1

			if diff == 1:
				acc += i
	return acc