#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	# One easy way is to just calculate the laviathan distance and if its 1 then subtract 2 from the upper limit
	limit = len(data) * 6

	checks = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

	for cube in data:
		x, y, z = map(int, cube.split(','))

		for dx, dy, dz in checks:
			nx, ny, nz = x + dx, y + dy, z + dz
			if f"{nx},{ny},{nz}" in data:
				limit -= 1
	
	return limit

def part2(data):
	# Will be solved using flood-fill
	cubes = []
	maxX = float('-inf')
	maxY = float('-inf')
	maxZ = float('-inf')

	for cube in data:
		x, y, z = map(int, cube.split(','))
		maxX = max(maxX, x)
		maxY = max(maxY, y)
		maxZ = max(maxZ, z)
		cubes.append((x, y, z))
	
	maxX, maxY, maxZ = maxX + 2, maxY + 2, maxZ + 2 # <- God knows why I have a two off error!
	
	# print(f'{maxX}x{maxY}x{maxZ} grid')

	surface = 0 # The number of times we hit the cube during the flood fill

	checks = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
	queue = [(-1, -1, -1)]
	visited = set()

	while queue:
		x, y, z = queue.pop(0)
		
		for dx, dy, dz in checks:
			nx, ny, nz = x + dx, y + dy, z + dz
			if not (-1 <= nx < maxX and -1 <= ny < maxY and -1 <= nz < maxZ): continue
			if f"{nx},{ny},{nz}" in visited: continue
			if (nx, ny, nz) in cubes:
				surface += 1
				continue
			queue.append((nx, ny, nz))
			visited.add(f"{nx},{ny},{nz}")

	return surface