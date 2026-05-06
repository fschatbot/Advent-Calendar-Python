#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import product

split_data = True
completed = 1
raw_data = None # Not To be touched

numericPad = {
	'7': (0, 0),
	'8': (1, 0),
	'9': (2, 0),
	'4': (0, 1),
	'5': (1, 1),
	'6': (2, 1),
	'1': (0, 2),
	'2': (1, 2),
	'3': (2, 2),
	'0': (1, 3),
	'A': (2, 3)
}

directionPad = {
	'^': (1, 0),
	'A': (2, 0),
	'<': (0, 1),
	'v': (1, 1),
	'>': (2, 1)
}

def generate_paths(code, pad) -> list[list[str]]:
	start = pad['A']
	path_options = []
	for c in code:
		paths = []
		pos = pad[c]
		move_x = ">" if pos[0] - start[0] > 0 else "<"
		move_y = "v" if pos[1] - start[1] > 0 else "^"
		dx = +1 if pos[0] - start[0] > 0 else -1
		dy = +1 if pos[1] - start[1] > 0 else -1


		def backtrack(path, a, b, x, y):
			if (x,y) not in pad.values():
				return
			if a == 0 and b == 0:
				paths.append(path+"A")
				return
			if a > 0:
				backtrack(path + move_x, a-1, b, x+dx, y)
			if b > 0:
				backtrack(path + move_y, a, b-1, x, y+dy)
		
		backtrack("", abs(pos[0] - start[0]), abs(pos[1] - start[1]), start[0], start[1])
		# Now we go through and verify that each path is on the keypad at all times.
		path_options.append(paths)
		
		start = pos
	
	return path_options

def options_comb(options):
	# def backtrack
	...


def part1(data):

	

	# What did I just end up reading...
	complexity = 0
	distribution = []
	for code in data:
		distribution.append([])
		# The only possible method is to figure out all the possible paths...
		# This then can be put through A* where score == the distance between the keys being pressed
		# So 029A has the distance of 8
		# <A^A>^^AvvvA has a distance of 28
		# v<<A>>^A<A>AvA<^AA>A<vAAA>^A has a distance of 68 (<- Thus creating the shortest path)

		# Figure out all possible methods of tying the code...
		# Then start from the smallest distance score and figure out all the paths
		# The distance score of those paths will now need to be minized...

		# Optimization whilst calculating the distance paths and possible paths would help prune out the sequence quickly...
		shortest = float('inf')

		pad1_opt = generate_paths(code, numericPad)
		# Now we need to permute through the options and select the best one
		for perm1 in product(*pad1_opt):
			path_1 = ''.join(perm1)
			pad2_opt = generate_paths(path_1, directionPad)
			for perm2 in product(*pad2_opt):
				path_2 = ''.join(perm2)
				# if len(path_2) > shortest: continue
				pad3_opt = generate_paths(path_2, directionPad)
				for perm3 in product(*pad3_opt):
					path_3 = ''.join(perm3)
					distribution[-1].append(len(path_3))
					if len(path_3) < shortest:
						shortest = len(path_3)
		complexity += shortest * int(code[:-1])


	return complexity

def part2(data):
	...