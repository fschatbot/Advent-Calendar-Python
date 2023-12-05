#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Tuple, Dict, Annotated

def proccess_data(data):
	data = data.split('\n\n')
	seeds = [int(seed) for seed in data[0].split(':')[1].strip().split(' ')]
	mappings = {}
	for rule in data[1:]:
		ruleName, ruleSet = rule.split('\n', 1)
		ruleName = ruleName.split(' ')[0]
		rulings = [[int(r) for r in ruling.split(' ')] for ruling in ruleSet.split('\n')]
		mappings[ruleName] = rulings
	return seeds, mappings

split_data = proccess_data
completed = 1
raw_data = None # Not To be touched

def part1(data:Tuple[List[int], Dict[str, List[Annotated[List[int], 3]]]]) -> int:
	seeds, mappings = data

	LowestLoc = None
	for seed in seeds:
		mappedNum = seed
		for maps in mappings.values():
			for destinationStart, sourceStart, rang in maps:
				if sourceStart <= mappedNum < sourceStart + rang:
					mappedNum = mappedNum + (destinationStart - sourceStart) # Add the offset
					break
		LowestLoc = min(LowestLoc, mappedNum) if LowestLoc else mappedNum
	return LowestLoc

def part2(data:Tuple[List[int], Dict[str, List[Annotated[List[int], 3]]]]) -> int:
	seeds, mappings = data
	seeds = [[seeds[i], seeds[i]+seeds[i+1]] for i in range(0, len(seeds), 2)]

	# Can be solved using range solving
	# 1. See if the seed range and the map range intersect (easy-medium) [Done]
	# 2. If so, then split the seed range into 2-3 sections, one with the map range and one with the original seed range (hard)
	# 3. Substitue the mapped range to this. (easy)
	# 4. Take the entire range of filling and quickly calculate the smallest number (easy)
	
	def intersects(a:Annotated[List[int], 2], b:Annotated[List[int], 2]) -> bool:
		"""Checks if the range b is intersecting with the range a"""
		a_start, a_end = a
		b_start, _ = b
		return a_start <= b_start <= a_end
	