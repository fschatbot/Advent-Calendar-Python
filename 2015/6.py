import numpy as np

split_data = True
completed = True
raw_data = None # Not To be touched

def proccess(line):
	p1, p2 = line.split(' through ')
	x1, x2 = p1.split(',')
	y1, y2 = p2.split(',')
	return int(x1), int(y1), int(x2), int(y2)

def part1(data):
	"""The Code is supposed to run here"""
	grid = np.zeros((1000, 1000), dtype=bool) # True represents lit and False represents off
	for line in data:
		if line.startswith('toggle'):
			x1, y1, x2, y2 = proccess(line.lstrip('toggle '))
			grid[x1:y1+1, x2:y2+1] = ~grid[x1:y1+1, x2:y2+1]
		elif line.startswith('turn off'):
			x1, y1, x2, y2 = proccess(line.lstrip('turn off '))
			grid[x1:y1+1, x2:y2+1] = False
		elif line.startswith('turn on'):
			x1, y1, x2, y2 = proccess(line.lstrip('turn on '))
			grid[x1:y1+1, x2:y2+1] = True
	return grid.sum()

def part2(data):
	"""The Code is supposed to run here"""
	grid = np.zeros((1000, 1000), dtype=int) # Creeate 2 dimensional grid of integers
	for line in data:
		if line.startswith('toggle'):
			x1, y1, x2, y2 = proccess(line.lstrip('toggle '))
			grid[x1:y1+1, x2:y2+1] += 2
		elif line.startswith('turn off'):
			x1, y1, x2, y2 = proccess(line.lstrip('turn off '))
			grid[x1:y1+1, x2:y2+1] -= 1
			# This makes it so the minimum requirement is 0. Hence removing all the negitive dimmed lighting
			# Even though it feels like it should be done later it is something to do now
			# It prevents situation like these
			# 0 - 1 + 1 should be 1 but doing it in the end would make it 0
			grid[x1:y1+1, x2:y2+1] = grid[x1:y1+1, x2:y2+1].clip(min=0)
		elif line.startswith('turn on'):
			x1, y1, x2, y2 = proccess(line.lstrip('turn on '))
			grid[x1:y1+1, x2:y2+1] += 1
	return grid.sum()