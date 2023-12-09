#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import heappush, heappop

split_data = True
completed = True
raw_data = None # Not To be touched

class Posv1:
	def __init__(self, pos, map, prevRisk:int) -> None:
		self.pos = pos
		self.map = map
		self.dist = (len(map[0]) - pos[0] - 1) + (len(map) - pos[1] - 1) # Manhattan distance
		self.risk = prevRisk + int(map[pos[1]][pos[0]])
	
	def newMoves(self):
		for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			nx, ny = self.pos[0] + dx, self.pos[1] + dy
			if 0 <= nx < len(self.map[0]) and 0 <= ny < len(self.map):
				yield Posv1((nx, ny), self.map, self.risk)
	
	def __lt__(self, other:"Posv1") -> bool:
		return self.risk + self.dist < other.risk + other.dist

def part1(data):
	# While the algorithm returns a path, its simply not good enough
	queue = [Posv1((0, 0), data, 0)]
	goal = (len(data[0]) - 1, len(data) - 1)
	seen = []
	while len(queue) > 0:
		item = heappop(queue)
		for newItem in item.newMoves():
			if newItem.pos == goal:
				return newItem.risk - int(data[0][0])
			if newItem.pos in seen: continue # For now we will ignore this
			heappush(queue, newItem)
			seen.append(newItem.pos)

def getMapRisk(map, pos):
	mx, my = len(map[0]), len(map)
	risk = int(map[pos[1] % my][pos[0] % mx]) # Getting the actual risk
	add = (pos[1] // my) + (pos[0] // mx) # Getting the additional points
	return (((risk + add) - 1) % 9 + 1) # Wrapping the risk back to original


class Posv2:
	def __init__(self, pos, map, prevRisk:int, nodes) -> None:
		self.pos = pos
		self.map = map
		self.dist = (5*len(map[0]) - pos[0] - 1) + (5*len(map) - pos[1] - 1) # Manhattan distance
		self.risk = prevRisk + getMapRisk(map, pos)
		self.nodes = nodes + [pos]
	
	def newMoves(self):
		for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			nx, ny = self.pos[0] + dx, self.pos[1] + dy
			if 0 <= nx < 5 * len(self.map[0]) and 0 <= ny < 5 * len(self.map):
				yield Posv2((nx, ny), self.map, self.risk, self.nodes)
	
	def __lt__(self, other:"Posv2") -> bool:
		return self.risk + self.dist < other.risk + other.dist

def part2(data):
	# Same thing as part1 expect for the few changes
	# 2. Changed the map size (required change)
	# 3. Everytime we get an item we add it to seen with its risk
	#  ├> We add it to queue only if the risk is below what is seen
	#  ╰> Due to this if we are running a queue item with risk above record we terminate that node
	queue = [Posv2((0, 0), data, 0, [])]
	goal = (5 * len(data[0]) - 1, 5 * len(data) - 1)

	seen = {}
	while len(queue) > 0:
		item = heappop(queue)
		if item.risk > seen.get(item.pos, float('Inf')): continue
		for newItem in item.newMoves():
			if newItem.pos == goal:
				return newItem.risk - int(data[0][0])
			
			if newItem.pos not in seen or newItem.risk < seen[newItem.pos]:
				heappush(queue, newItem)
				seen[newItem.pos] = newItem.risk