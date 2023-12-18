#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

split_data = ','
completed = True
raw_data = None # Not To be touched

def hashStr(str:str) -> int:
	curr = 0
	for char in str:
		curr += ord(char)
		curr *= 17
		curr %= 256
	return curr


def part1(data:List[str]):
	acc = 0
	for line in data:
		acc += hashStr(line)
	return acc

def part2(data:List[str]):
	hashmap = {i: [] for i in range(256)}
	for line in data:
		if line[-1] == '-':
			box = hashStr(line[:-1])
			hashmap[box] = [lens for lens in hashmap[box] if lens['label'] != line[:-1]]
		elif line[-2] == '=':
			box = hashStr(line[:-2])
			for lens in hashmap[box]:
				if lens['label'] == line[:-2]:
					lens['focal'] = int(line[-1])
					break
			else:
				hashmap[box].append({'label': line[:-2], 'focal': int(line[-1])})
		else:
			print('How did we get here?')
			print(line)
	
	acc = 0
	for box, lens in hashmap.items():
		for slot, len in enumerate(lens, start=1):
			acc += (box + 1) * (slot) * (len['focal'])
	
	return acc