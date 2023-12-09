#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	acc = 0
	for line in data:
		seqMap = [[int(x) for x in line.split(' ')]]
		while not all(x == 0 for x in seqMap[-1]):
			new_map = []
			for seq1, seq2 in zip(seqMap[-1][:-1], seqMap[-1][1:]):
				new_map.append(seq2 - seq1)
				
			seqMap.append(new_map)
		acc += sum(seq[-1] for seq in seqMap)

	return acc

def part2(data):
	acc = 0
	for line in data:
		seqMap = [[int(x) for x in line.split(' ')]]
		while not all(x == 0 for x in seqMap[-1]):
			new_map = []
			for seq1, seq2 in zip(seqMap[-1][:-1], seqMap[-1][1:]):
				new_map.append(seq2 - seq1)
				
			seqMap.append(new_map)
		
		# Just need to subtract curr from the above sequences first value
		a = 0
		for seq in seqMap[::-1][1:]:
			a = seq[0] - a
		acc += a

	return acc