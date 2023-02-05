#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .intcode import computer5
# import os

split_data = ','
completed = 1
raw_data = None # Not To be touched

def part1(data):
	computer = computer5.from_instructions(data)
	computer.run_till_end()
	return sum(output == 2 for output in computer.outs[2::3])

# def displayMap(tiles):
# 	"This function exists in case you want to watch the game unfold"

# 	# Find the size of the map
# 	xMax = max(x for x, _ in tiles.keys())
# 	yMax = max(y for _, y in tiles.keys())

# 	# Display the map
# 	print_output = ''
# 	for y in range(0, yMax + 1):
# 		for x in range(0, xMax + 1):
# 			if (x, y) not in tiles:
# 				print_output += ' '
# 			elif tiles[(x, y)] == 0:
# 				print_output += ' '
# 			elif tiles[(x, y)] == 1:
# 				print_output += '█'
# 			elif tiles[(x, y)] == 2:
# 				print_output += '▒'
# 			elif tiles[(x, y)] == 3:
# 				print_output += '▁'
# 			elif tiles[(x, y)] == 4:
# 				print_output += '●'
# 		print_output += '\n'
# 	os.system('cls' if os.name == 'nt' else 'clear')
# 	print(print_output)


def proccessOutput(output):
	xPos = output[::3]
	yPos = output[1::3]
	tile = output[2::3]

	tiles = {}
	score = 0
	ball = None, None
	paddle = None, None
	for x, y, tile in zip(xPos, yPos, tile):
		if x == -1 and y == 0:
			score = tile
			continue
		if tile == 4:
			ball = x, y
		if tile == 3:
			paddle = x, y
		tiles[(x, y)] = tile
	
	gameOver = all(tile != 2 for tile in tiles.values())
	# displayMap(tiles)

	return score, ball, paddle, gameOver


def part2(data):
	data[0] = 2
	computer = computer5.from_instructions(data)
	score, ball, paddle, gameOver = 0, (None, None), (None, None), False
	while not gameOver:
		computer.run_till_input()
		score, ball, paddle, gameOver = proccessOutput(computer.outs)

		if ball[0] < paddle[0]:
			computer.input(-1)
		elif ball[0] > paddle[0]:
			computer.input(1)
		else:
			computer.input(0)
	
	return score