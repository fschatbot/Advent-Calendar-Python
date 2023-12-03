#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parser(data):
	gameInfo = []
	for line in data.split('\n'):
		# Hint: The blocks were placed back in the bag after each set
		SetList = line.split(': ')[1]
		lineInfo = {}
		for BlockSet in SetList.split('; '):
			for block in BlockSet.split(', '):
				count, name = block.split(' ')
				lineInfo[name] = max(lineInfo.get(name, 0), int(count))
		
		gameInfo.append(lineInfo)
	
	return gameInfo


split_data = parser
completed = True
raw_data = None # Not To be touched

def part1(data) -> int:
	acc = 0
	for gameId, BlockData in enumerate(data, start=1):
		if len(BlockData) == 3 and BlockData.get('red', 100) <= 12 and BlockData.get('green', 100) <= 13 and BlockData.get('blue', 100) <= 14:
			acc += int(gameId)
	return acc

def part2(data) -> int:
	acc = 0
	for BlockData in data:
		counter = 1
		for item in BlockData.values(): counter *= item	
		acc += counter
	return acc