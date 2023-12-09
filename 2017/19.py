#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

split_data = True
completed = True
raw_data = None # Not To be touched

class DIRECTION:
	UP    = [0, -1]
	DOWN  = [0, +1]
	LEFT  = [-1, 0]
	RIGHT = [+1, 0]

def part1(data:List[str]):
	checkpoints = ''
	direction = DIRECTION.DOWN
	pos = [data[0].index('|'), 0]

	def getPos(pos):
		if 0 <= pos[0] < len(data[0]) and 0 <= pos[1] < len(data):
			return data[pos[1]][pos[0]]
		else:
			return ' '

	while getPos(pos) != ' ':
		char = getPos(pos)
		if char not in ('-', '+', '|'):	checkpoints += char # Adding character to checkpoint

		if char not in (' ', '+'): # Continuting till we reach a turn
			pos[0] += direction[0]
			pos[1] += direction[1]
		elif char == '+':
			for newDir in (DIRECTION.UP, DIRECTION.RIGHT, DIRECTION.DOWN, DIRECTION.LEFT): # Checking clockwise
				if newDir == [-dir for dir in direction]: continue # Skip check if came from there
				newPos = [pos[0] + newDir[0], pos[1] + newDir[1]]
				if getPos(newPos) != ' ':
					pos = newPos
					direction = newDir
					break
			else:
				return
		else:
			print('Somehow the code has nowhere to go!', pos)
			return
	return checkpoints

def part2(data):
	checkpoints = ''
	direction = DIRECTION.DOWN
	pos = [data[0].index('|'), 0]
	steps = 0

	def getPos(pos):
		if 0 <= pos[0] < len(data[0]) and 0 <= pos[1] < len(data):
			return data[pos[1]][pos[0]]
		else:
			return ' '

	while getPos(pos) != ' ':
		char = getPos(pos)
		if char not in ('-', '+', '|'):	checkpoints += char # Adding character to checkpoint

		if char not in (' ', '+'): # Continuting till we reach a turn
			pos[0] += direction[0]
			pos[1] += direction[1]
		elif char == '+':
			for newDir in (DIRECTION.UP, DIRECTION.RIGHT, DIRECTION.DOWN, DIRECTION.LEFT): # Checking clockwise
				if newDir == [-dir for dir in direction]: continue # Skip check if came from there
				newPos = [pos[0] + newDir[0], pos[1] + newDir[1]]
				if getPos(newPos) != ' ':
					pos = newPos
					direction = newDir
					break
			else:
				return
		else:
			print('Somehow the code has nowhere to go!', pos)
			return
		steps += 1
	return steps