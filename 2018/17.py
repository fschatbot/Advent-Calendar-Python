#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def parse(data):
	map = {}

	for line in data.split('\n'):
		staticVariable, staticValue, _, dynamicStart, dynamicEnd = re.search(r'(\w)=(\d+), (\w)=(\d+)\.\.(\d+)', line).groups()
		staticValue, dynamicStart, dynamicEnd = int(staticValue), int(dynamicStart), int(dynamicEnd)
		for dynamicValue in range(dynamicStart, dynamicEnd+1):
			if staticVariable == 'x':
				map[(staticValue, dynamicValue)] = '#'
			else:
				map[(dynamicValue, staticValue)] = '#'
	
	map[(500, 0)] = '+'
	return map

split_data = parse
completed = True
raw_data = None # Not To be touched

def print_map(map):
	rowstart = min(pos[0] for pos in map.keys())
	rowlen = max(pos[0] for pos in map.keys())
	collen = max(pos[1] for pos in map.keys())
	
	lines = []
	for y in range(0, collen + 1):
		lines.append('')
		for x in range(rowstart-1, rowlen+2):
			lines[-1] += map.get((x,y), '.')
	
	with open('2018/inputs/17.debug.txt', 'w') as file:
		file.write('\n'.join(lines))

def simulate(map):
	# The principal is to compare the old and new map to see if any change has been made
	# Step 1: Spawn a waterBlock at the top
	# Step 2: Keep looping through the waterblocks till all of them hit a dead end
	# Step 2.1: Move the water block till it returns a value or hits a dead-end
	# Step 2.1a: If tuple then it is a sign to check for still water at the given position (additional dx helps us quickly find the direction)
	# Step 2.1b: If list then it is a bunch of children. Add these children to the waterblocks list if they haven't been added before
	# Step 3: Loop through the "supposed" still water coordinates and confirm and mark them if they are between 2 clay blocks
	# Return the map if the old and the new are the same

	# Water block movement:
	# Mark the current position as flowing water
	# If can move down it will move down
	# If hit still water or clay whilst moving down return 2 water blocks that will spread in either direction
	# If moving sideways but can go down then change the direction
	# If hit clay whilst moving sideways then request a check for still water
	# If going below the deepest clay then consider it dead
	# If no problem encountered then mark the new coordinates as the current coordinates

	limit = max(pos[1] for pos in map.keys())
	
	old_map = {}
	map = map

	class waterBlock:
		def __init__(self, x, y, dx, dy):
			self.x = x
			self.y = y
			self.dx = dx
			self.dy = dy
			self.dead = False
		
		def move(self):
			map[(self.x, self.y)] = '|'

			nx, ny = self.x + self.dx, self.y + self.dy
			if self.dy == 1 and map.get((nx, ny)) in ('#', '~'):
				# Spreading water
				self.dead = True
				return [waterBlock(self.x, self.y, -1, 0), waterBlock(self.x, self.y, 1, 0)]
			elif self.dy == 0 and map.get((self.x, self.y+1)) in (None, '|'):
				# Changing water direction
				self.dx = 0
				self.dy = 1
			elif self.dy == 0 and map.get((nx, ny)) == '#':
				# Hit dead-end when spreading
				self.dead = True
				return (self.x, self.y, self.dx * -1)
			elif ny > limit:
				self.dead = True
			else:
				# We can continue
				self.x = nx
				self.y = ny
		
		def moveFull(self):
			output = None
			while not self.dead and output == None:
				output = self.move()
			return output

	
	while old_map != map:
		old_map = dict(map)

		waterBlocks = [waterBlock(500, 1, 0, 1)]
		fixWater = []
		ignoreChildren = []
		while any(not water.dead for water in waterBlocks):
			for water in waterBlocks:
				if water.dead: continue

				children = water.moveFull()
				# tuple = fixWater coordinate, list = children
				if type(children) == tuple:
					fixWater.append(children)
				elif children:
					for child in children:
						if (child.x, child.y, child.dx, child.dy) in ignoreChildren: continue
						ignoreChildren.append((child.x, child.y, child.dx, child.dy))
						waterBlocks.append(child)
			waterBlocks = [water for water in waterBlocks if not water.dead]
		# Putting some water at rest
		for potentialRest in fixWater:
			x, y, dx = potentialRest
			new_pos = x, y
			while map.get(new_pos) != '#':
				if map.get(new_pos) != '|': break # We have reached dry sand
				new_pos = new_pos[0] + dx, new_pos[1]
			else:
				# If we successfully reached till a clay block
				for x in range(x, new_pos[0], dx):
					map[(x, y)] = '~'
	
	return map


def part1(data):
	simulatedMap = simulate(data)
	# print_map(simulatedMap)

	topmost_y = min(point[1] for point in data if data[point] == '#') # y coord for the clay closest to the surface
	return sum(1 for position, mapData in simulatedMap.items() if mapData in ('|', '~') and position[1] >= topmost_y)

def part2(data):
	simulatedMap = simulate(data)
	# print_map(simulatedMap)

	topmost_y = min(point[1] for point in data if data[point] == '#') # y coord for the clay closest to the surface
	return sum(1 for position, mapData in simulatedMap.items() if mapData == '~' and position[1] >= topmost_y)