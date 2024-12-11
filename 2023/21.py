#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Tuple

def parse(data):
	starting = None
	walls = []

	for y, line in enumerate(data.split('\n')):
		for x, char in enumerate(line):
			if char == '#': walls.append((x, y))
			if char == 'S': starting = x, y
	
	return walls, starting, (len(data.split('\n')[0]), len(data.split('\n')))

split_data = parse
completed = 1
raw_data = None # Not To be touched

class DIRECTION:
	UP    = [0, -1]
	DOWN  = [0, +1]
	LEFT  = [-1, 0]
	RIGHT = [+1, 0]


def prettyPrint(walls, mx, my, new_at):
	for y in range(my):
		string = ''
		for x in range(mx):
			if (x, y) in new_at:
				string += 'O'
			elif (x, y) in walls:
				string += '#'
			else:
				string += '.'
		
		print(string)
	print()

def part1(data:Tuple[List[Tuple[int, int]], Tuple[int, int]]):
	walls, starting, mapsize = data
	mx, my = mapsize

	
	at = set()
	new_at = set([starting])
	for _ in range(64):
		at = new_at
		new_at = set()

		for x, y in at:
			for dx, dy in [DIRECTION.UP, DIRECTION.DOWN, DIRECTION.LEFT, DIRECTION.RIGHT]:
				nx, ny = x + dx, y + dy
				if not (0 <= nx < mx and 0 <= ny < my): continue
				if (nx, ny) in walls: continue
				new_at.add((nx, ny))
		
	prettyPrint(walls, mx, my, new_at)

	return len(new_at)

def part2(data:List[str]):
	# I think the trick to this is waiting for any one of the tiles the elf can be present at any given moment.
	# After this the adjecent tiles will be filled no matter the given step.
	# 2. We can find this tile by checking if the tile was present in the "at" set 2 times
	# Mathematical Approch	
	# We just need to find the amount of unique tiles it can reach by the end of 26501365 steps
	# Then return ans // 2 and we should be done. (Approximate)
	# Brute Approch
	# Figure out at which point after spreading indefinately does the the grid begin to repeat.
	# 2. When that happens we win
	# Elegant Approch:
	# Note: After the elf reach a point for the first time the elf can reach that step every other time!
	# Hence, after a point the grid will simply start repeating itself. The on will become off and the off will become on
	# Hence, we need to find a place only once and never ever think about it again.
	...