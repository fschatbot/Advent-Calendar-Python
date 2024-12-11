#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

split_data = True
completed = 1
raw_data = None # Not To be touched

class MOVEMENT:
	NORTH = ( 0, -1)
	SOUTH = ( 0, +1)
	WEST  = (-1,  0)
	EAST  = (+1,  0)

DirectionMap = {
	"|": [MOVEMENT.NORTH, MOVEMENT.SOUTH],
	"-": [MOVEMENT.WEST, MOVEMENT.EAST],
	"L": [MOVEMENT.NORTH, MOVEMENT.EAST],
	"J": [MOVEMENT.NORTH, MOVEMENT.WEST],
	"F": [MOVEMENT.SOUTH, MOVEMENT.EAST],
	"7": [MOVEMENT.SOUTH, MOVEMENT.WEST],
}

def part1(data:List[str]):
	mx, my = len(data[0]), len(data) # Just getting the boundings of the map!

	py = [i for i, line in enumerate(data) if 'S' in line][0]
	px = data[py].index('S')
	# print('Map Size   :', (mx, my))
	# print('Starting At:', start)

	nodes = [(px, py)] # All the pipes with the central connecting pipe
	curr = None
	# Determining the first move
	if data[py + 1][px] in ('|', 'L', 'J'): # South
		curr = (px, py+1)
	elif data[py - 1][px] in ('|', 'F', '7'): # North
		curr = (px, py-1)
	elif data[py][px + 1] in ('-', '7', 'J'): # East
		curr = (px + 1, py)
	elif data[py][px - 1] in ('-', 'L', 'F'): # West
		curr = (px - 1, py)
	
	
	# Keep going till we reach the first node
	while data[curr[1]][curr[0]] != 'S':
		movements = DirectionMap[data[curr[1]][curr[0]]]
		for dx, dy in movements:
			nx, ny = curr[0] + dx, curr[1] + dy
			if not (0 <= nx < mx and 0 <= ny < my): continue # Stay inbounds
			if (nx, ny) == nodes[-1]: continue # We came from here
			# Found the next movement
			nodes.append(curr)
			curr = nx, ny
			break
	# print(nodes, len(nodes))

	return len(nodes) // 2

def part2(data:List[str]):
	# The calculatation of the nodes' code is exactly the same 
	mx, my = len(data[0]), len(data) # Just getting the boundings of the map!

	py = [i for i, line in enumerate(data) if 'S' in line][0]
	px = data[py].index('S')

	nodes = [(px, py)] # All the pipes with the central connecting pipe
	curr = None
	# Determining the first move
	if data[py + 1][px] in ('|', 'L', 'J'): # South
		curr = (px, py+1)
	elif data[py - 1][px] in ('|', 'F', '7'): # North
		curr = (px, py-1)
	elif data[py][px + 1] in ('-', '7', 'J'): # East
		curr = (px + 1, py)
	elif data[py][px - 1] in ('-', 'L', 'F'): # West
		curr = (px - 1, py)
		
	# Keep going till we reach the S node
	while data[curr[1]][curr[0]] != 'S':
		movements = DirectionMap[data[curr[1]][curr[0]]]
		for dx, dy in movements:
			nx, ny = curr[0] + dx, curr[1] + dy
			if not (0 <= nx < mx and 0 <= ny < my): continue # Stay inbounds
			if (nx, ny) == nodes[-1]: continue # We came from here
			# Found the next movement
			nodes.append(curr)
			curr = nx, ny
			break
	
	# https://en.wikipedia.org/wiki/Nonzero-rule (This is how we should be solving this day!)
	# Much thanks to https://www.reddit.com/r/adventofcode/comments/18eza5g/comment/kcqwjon/
	# └ Info: The code wasn't copied. Only the concept was understood through the gif and explaintation provided!
	insideCounter = 0
	insiders = []

	for y in range(my):
		nonZeroCounter = 0 # Checking the from left-to-right direction!
		lastMove = 0
		for x in range(mx):
			if (x, y) in nodes:
				prevN = nodes[(nodes.index((x, y)) - 1) % len(nodes)] # Previous Node
				nextN = nodes[(nodes.index((x, y)) + 1) % len(nodes)] # Next Node
				diff = y - prevN[1] # -1 == UP, 1 == DOWN and 0 == LEFT/RIGHT
				if lastMove == -1: # We look at the exit
					diff = nextN[1] - y
				if diff == 0 or lastMove == diff: continue # Only care if the direct we came has changed
				if nonZeroCounter == 0 and diff == 1: continue
				nonZeroCounter += 1
				lastMove = diff
			elif nonZeroCounter % 2 == 1:
				insiders.append((x, y))
				insideCounter += 1
	
	# Generating and storing the simplified entire map in 2023/inputs/10.dump.txt
	"""
	pipeMap = []
	replaceMent = {
		'|': '│',
		'-': '─',
		'F': '┌',
		'7': '┐',
		'L': '└',
		'J': '┘',
		'S': 'S'
	}
	for y in range(my):
		pipeMap.append('')
		for x in range(mx):
			if (x, y) in nodes:
				pipeMap[-1] += replaceMent[data[y][x]]
			elif (x, y) in insiders:
				pipeMap[-1] += '#'
			else:
				pipeMap[-1] += '.'
	
	with open('2023/inputs/10.dump.txt', 'w', encoding='utf-8') as f:
		f.write('\n'.join(pipeMap))
	"""
	
	return insideCounter
