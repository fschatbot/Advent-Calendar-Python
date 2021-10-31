import numpy as np


split_data = True
raw_data = None # Not To be touched

def proccess(line):
	p1, p2 = line.split(' through ')
	x1, y1 = p1.split(',')
	x2, y2 = p2.split(',')
	return int(x1), int(y1), int(x2), int(y2)

def part1(data):
	"""The Code is supposed to run here"""
	grid = np.ndarray((1000, 1000), dtype=np.bool) # True represents lit and False represents off
	for line in data:
		if line.startswith('toggle'):
			x1, y1, x2, y2 = proccess(line.lstrip('toggle '))
			grid[x1:y1+1, x2:y2+1] = ~grid[x1:y1+1, x2:y2+1]
		elif line.startswith('turn off'):
			x1, y1, x2, y2 = proccess(line.lstrip('turn off '))
			grid[x1:y1+1, x2:y2+1] = True
		elif line.startswith('turn on'):
			x1, y1, x2, y2 = proccess(line.lstrip('turn off '))
			grid[x1:y1+1, x2:y2+1] = False
	print("The Answer to the First part is:", grid.sum())

def part2(data):
	"""The Code is supposed to run here"""
	pass


def main(puzzle_input):
	global raw_data
	raw_data = puzzle_input
	part1(raw_data.split('\n') if split_data else raw_data)
	part2(raw_data.split('\n') if split_data else raw_data)