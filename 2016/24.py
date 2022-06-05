#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import permutations
from functools import lru_cache

split_data = True
completed = True
raw_data = None # Not To be touched

def proccess_data(data):
	# Extract all the checkpoints and where we are going to start
	numCoords = {}
	for i, line in enumerate(data):
		for j, char in enumerate(line):
			if char == '0':
				startX, startY = j, i
			elif char not in ('.', '#'):
				numCoords[char] = (j, i)
	
	return numCoords, (startX, startY)

# BFS alogrithm to find the shortest path to the given goal
def bfs(queue, visited, dept, goal, grid):
	grid_size = len(grid[0]), len(grid)
	next_queue = []
	for coord in queue:
		# Now we try to move in all possible directions
		for mx, my in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			nx, ny = coord[0] + mx, coord[1] + my # nx = new X, ny = new Y
			# Make sure we are within the grid
			if not (0 <= nx < grid_size[0]) or not (0 <= ny < grid_size[1]) or (nx, ny) in visited: continue
			# If we hit the goal, return the dept
			elif (nx, ny) == goal:
				return dept
			# If the movement is not a wall, add it to the queue
			elif grid[ny][nx] != '#':
				next_queue.append((nx, ny))
				visited.append((nx, ny))
	
	# Return -1 if we can't find a path or have lit the reccursion limit
	# else continue with the next step
	if not next_queue:
		return -1
	try:
		return bfs(next_queue, visited, dept + 1, goal, grid)
	except RecursionError:
		return -1

# We can end up in the same situation twice
# So its best if we cache up the results
@lru_cache(maxsize=None)
def find_dept(start, end, grid):
	# This function works as a wrapper, making the BFS easier to use
	return bfs([start], [start], 1, end, grid)

def part1(data):
	numCoords, (startX, startY) = proccess_data(data)

	# We try every checkpoint path we can take
	# we also add a max limit, so if the path is longer then the limit, we can skip it
	Max = len(data[0]) * len(data) # This is the amount of squares in the grid, so the path is bound to be shorter
	
	for path in permutations(numCoords.keys()):
		score = 0
		currX, currY = startX, startY
		for checkpoint in path:
			dept = find_dept(numCoords[checkpoint], (currX, currY), tuple(data))
			if dept == -1: break # If we can't find a further path, then why bother with this permutation
			score += dept
			currX, currY = numCoords[checkpoint]
			if score >= Max:
				# The current path is much longer than the best path, so we don't need to take it
				break
		else:
			# If the path didn't exceed the limit, then we found a better path
			# We set it as the best score and move forward
			# print("Best Path:", score)
			Max = score
	return Max


def part2(data):
	# Difference between part1 and part2? Nothing except for the fact that we need to return to 0 again
	# The change in the code will be marked with a comment
	# On the plus side, the code will be slightly faster as the part1 would have cached a lot of things
	

	numCoords, (startX, startY) = proccess_data(data)
	numCoords['0'] = (startX, startY) # We simply add the start point to the list of checkpoints

	Max = len(data[0]) * len(data)
	
	for path in permutations(num for num in numCoords.keys() if num != '0'): # We don't pass in the checkpoint '0' for permutation
		path = path + ('0',) # So that we can add it at the end as its fixed
		score = 0
		currX, currY = startX, startY
		for checkpoint in path:
			dept = find_dept(numCoords[checkpoint], (currX, currY), tuple(data))
			if dept == -1: break
			score += dept
			currX, currY = numCoords[checkpoint]
			if score >= Max:
				break
		else:
			Max = score
	return Max