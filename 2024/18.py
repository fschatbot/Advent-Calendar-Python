#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import heappop, heappush

def parse(data):
	points = []
	for point in data.split('\n'):
		x, y = point.split(',')
		points.append((int(x), int(y)))
	
	return points

split_data = parse
completed = True
raw_data = None # Not To be touched

def part1(data):
	movements = [(0, -1), (0, 1), (1, 0), (-1, 0)]
	mapSize = 71
	goal = (70,70)
	corrupted = data[:1024]


	seen = set()
	queue = [(0,0,0, [(0,0)])]
	while len(queue) > 0:
		x, y, steps, path = queue.pop(0)

		for dx, dy in movements:
			nx, ny = x + dx, y + dy
			if not (0 <= nx < mapSize and 0 <= ny < mapSize): continue
			if (nx, ny) in seen: continue
			if (nx, ny) in corrupted: continue
			if (nx, ny) == goal:
				# plot(path+[goal], corrupted, mapSize)
				return steps+1

			seen.add((nx, ny))
			queue.append((nx, ny, steps+1, path+[(nx, ny)]))
	
	print(seen)
	print(f"WTF? We saw {len(seen)} locations and still haven't seen the goal!")

def plot(path, walls, size):
	for y in range(size):
		for x in range(size):
			if (x, y) in walls:
				print('#', end='')
			elif (x, y) in path:
				print('O', end='')
			else:
				print('.', end='')
		print()

def hasPath(start, end, blocked, bounds):
	# Since we don't care much about optimality, this we will implement the A* algorithm
	movements = [(0, -1), (0, 1), (1, 0), (-1, 0)]
	(sx, sy), (ex, ey) = start, end

	seen = set()
	queue = [(abs(ex-sx)+abs(ey-sy), sx, sy, id(0), [sx, sy])] # Heuristic, x, y, unique, path
	while len(queue) > 0:
		_, x, y, _, path = heappop(queue)

		for dx, dy in movements:
			nx, ny = x + dx, y + dy
			if not (0 <= nx < bounds[0] and 0 <= ny < bounds[1]): continue
			if (nx, ny) in seen: continue
			if (nx, ny) in blocked: continue
			if (nx, ny) == end: return path+[end]

			seen.add((nx, ny))
			heappush(queue, (abs(ex-nx)+abs(ey-ny), nx, ny, id(0), path+[(nx, ny)]))
	
	return False

def part2(data):
	checking = 1024
	path = hasPath((0, 0), (70, 70), data[:checking], (71, 71))
	while True:
		checking += 1
		if data[checking-1] in path: # Only update if the current byte disturbs the precalculated path (optimization)
			path = hasPath((0, 0), (70, 70), data[:checking], (71, 71))
			if path == False:
				# plot(hasPath((0, 0), (70, 70), data[:checking-1], (71, 71)), data[:checking], 71)
				break
			# plot(path, data[:checking], 71)
			# print('---')
		
		# if checking % 100 == 0: print(f'{checking/len(data):,.2%}')
	
	return f'{data[checking-1][0]},{data[checking-1][1]}'