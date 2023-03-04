#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .intcode import computer6
from typing import List

split_data = ','
completed = True
raw_data = None # Not To be touched

# Showcase the entire map in the console
def print_map(visited):
	minX = min([x[0] for x in visited.keys()])
	maxX = max([x[0] for x in visited.keys()])
	minY = min([x[1] for x in visited.keys()])
	maxY = max([x[1] for x in visited.keys()])
	print('MinX: {}, MaxX: {}, MinY: {}, MaxY: {}'.format(minX, maxX, minY, maxY))

	for y in range(minY-1, maxY+1):
		for x in range(minX-1, maxX+1):
			if (x, y) == (0, 0):
				print('S', end='')
			if (x, y) in visited:
				if visited[(x, y)] == 0:
					print('#', end='')
				elif visited[(x, y)] == 1:
					print('.', end='')
				elif visited[(x, y)] == 2:
					print('O', end='')
			else:
				print(' ', end='')
		print()

def part1(data):
	# The way we are going to solve this day is by using a BFS algorithm
	moveMap = {
		1: (0, 1),
		2: (0, -1),
		3: (-1, 0),
		4: (1, 0)
	}
	

	def BFS(queue:List[computer6], visited, dept):
		next_queue = [] # The next move to take
		for computer in queue: # For each coordinate in the queue
			for i in range(1, 5): # For each direction
				# Check if we have been there before
				coord = computer.extra_memory['coord']
				movement = coord[0] + moveMap[i][0], coord[1] + moveMap[i][1]
				if movement in visited: continue

				# Seems like we haven't been there before, lets try it out
				new_comp = computer.copy()
				new_comp.input(i)
				output = new_comp.run_till_output()

				if output == 0:
					# Its a wall
					visited[movement] = 0
				elif output == 1:
					# We can move there
					new_comp.extra_memory['coord'] = movement
					next_queue.append(new_comp)
					visited[movement] = 1
				elif output == 2:
					# We have found the oxygen system
					visited[movement] = 2
					# print_map(visited)
					return dept + 1
				
		return BFS(next_queue, visited, dept+1)
	
	curr_computer = computer6.from_instructions(data)
	curr_computer.extra_memory['coord'] = (0, 0)
	
	return BFS([curr_computer], {(0, 0): 1}, 0)


def part2(data):
	# The way to solve this is simple
	# First we get the full map of the area
	# Next we find the furthest point from the oxygen system because the oxygen will reach it the last
	# The distance will be our answers

	# The way we are going to solve this day is by using a BFS algorithm
	moveMap = {
		1: (0, 1),
		2: (0, -1),
		3: (-1, 0),
		4: (1, 0)
	}
	
	# The only change in the alogrithm is that it will now keep going until it has found all the points
	# instead of stopping when it found the oxygen system
	def BFS(queue:List[computer6], visited, dept):
		next_queue = [] # The next move to take
		for computer in queue: # For each coordinate in the queue
			for i in range(1, 5): # For each direction
				# Check if we have been there before
				coord = computer.extra_memory['coord']
				movement = coord[0] + moveMap[i][0], coord[1] + moveMap[i][1]
				if movement in visited: continue

				# Seems like we haven't been there before, lets try it out
				new_comp = computer.copy()
				new_comp.input(i)
				output = new_comp.run_till_output()

				if output == 0:
					# Its a wall
					visited[movement] = 0
				elif output == 1:
					# We can move there
					new_comp.extra_memory['coord'] = movement
					next_queue.append(new_comp)
					visited[movement] = 1
				elif output == 2:
					# We have found the oxygen system
					new_comp.extra_memory['coord'] = movement
					next_queue.append(new_comp)
					visited[movement] = 2
		
		if len(next_queue) == 0: return visited
				
		return BFS(next_queue, visited, dept+1)
	
	curr_computer = computer6.from_instructions(data)
	curr_computer.extra_memory['coord'] = (0, 0)

	fullMap = BFS([curr_computer], {(0, 0): 1}, 0)

	# Now we need to find the furthest point from the oxygen system
	# We will do this by using a BFS algorithm from that point that keeps going until it has found all the points
	# The dept at which it touches all the points will be our answer

	def BFS2(queue:List[tuple], visited, dept):
		next_queue = [] # The next move to take
		for coord in queue: # For each coordinate in the queue
			for i in range(1, 5): # For each direction
				# Check if we have been there before
				movement = coord[0] + moveMap[i][0], coord[1] + moveMap[i][1]
				if movement in visited: continue

				# Seems like we haven't been there before, lets try it out
				if fullMap[movement] == 1:
					next_queue.append(movement)
					visited[movement] = True

		if len(next_queue) == 0: return dept

		return BFS2(next_queue, visited, dept+1)
	
	# Find the oxygen system
	oxygen_system = [coord for coord, val in fullMap.items() if val == 2][0]
	return BFS2([oxygen_system], {oxygen_system: True}, 0)
