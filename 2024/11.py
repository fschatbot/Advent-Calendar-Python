#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
from functools import lru_cache
from collections import Counter

split_data = ' '
completed = True
raw_data = None # Not To be touched

def part1(data:List[str]):
	stones = data

	for _ in range(25):
		newStones = []

		for stone in stones:
			if stone == '0':
				newStones.append('1')
			elif len(stone) % 2 == 0:
				mid = len(stone) // 2
				left, right = stone[:mid], stone[mid:]
				# str -> int -> str to remove trailing 0
				newStones.append(str(int(left)))
				newStones.append(str(int(right)))
			else:
				newStones.append(str(int(stone)*2024))
		
		stones = newStones
	
	return len(stones)

def part2(data:List[str]):
	# We can speed up the entire thing by grouping the same stones together

	@lru_cache(None, typed=False)
	def resolve(stone:str) -> List[str]:		
		if stone == '0':
			return ['1']
		elif len(stone) % 2 == 0:
			mid = len(stone) // 2
			left, right = stone[:mid], stone[mid:]
			# str -> int -> str to remove trailing 0
			return [str(int(left)), str(int(right))]
		else:
			return [str(int(stone)*2024)]
	
	stones = Counter(data)

	for _ in range(75):
		newStones = Counter()
		for stone, value in stones.items():
			resolved = {s:v*value for s, v in Counter(resolve(stone)).items()}
			newStones.update(resolved)
		
		stones = newStones

	print(resolve.cache_info())

	return stones.total()