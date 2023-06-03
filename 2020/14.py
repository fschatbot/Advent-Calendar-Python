#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import product

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	mask = ""
	mem = {}

	for line in data:
		if line.startswith('mask'):
			mask = line.split('=')[1].strip()
		else:
			memIndexLine, value = line.split('=')
			memIndex = int(memIndexLine[4:-2])
			val = int(value)
			for i, v in enumerate(mask):
				if v == 'X':
					pass
				elif v == '1':
					val = val | (2 ** (36 - i - 1))
				elif v == '0':
					val = val & ~(2 ** (36 - i - 1))
			mem[memIndex] = val # Just for the sake of it
	
	return sum(mem.values())

def part2(data):
	mask = ""
	mem = {}

	for line in data:
		if line.startswith('mask'):
			mask = line.split('=')[1].strip()
		else:
			memIndexLine, value = line.split('=')
			memIndex = int(memIndexLine[4:-2])
			val = int(value)
			indexB = format(memIndex, 'b').rjust(36, '0')
			maskedIndex = ''.join(v if v != '0' else indexB[i] for i, v in enumerate(mask))
			for replacement in product('01', repeat=maskedIndex.count('X')):
				index = str(maskedIndex)
				for possiblity in replacement:
					index = index.replace('X', possiblity, 1)
				mem[int(index, 2)] = val
	return sum(mem.values())