#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from itertools import combinations

def parse(data):
	floors = {floor: [] for floor in range(1, 5)}
	for index, line in enumerate(data.split('\n'), start=1):
		if "nothing relevant" in line: continue
		items = re.findall(r'(a [^,.]+)', line.replace('and', ','))
		items = [item.replace('-compatible', '').strip(' a') for item in items]
		items = [item.replace('generator', 'G').replace('microchip', 'M') for item in items]
		floors[index] = items
	return floors

split_data = parse
completed = 1
raw_data = None # Not To be touched

def hashTheMap(map, elevator:int) -> str:
	# Replace all generator and microchip items with "G&M" as pairs are interchangeable
	newFloors = []
	for floor in map.values():
		new_floor = []
		for item in floor:
			if item[-1] == 'M' and item[:-1]+'G' in floor:
				new_floor.append('G&M')
			elif item[-1] == 'G' and item[:-1]+'M' in floor:
				continue
			else:
				new_floor.append(item)
		new_floor.sort()
		newFloors.append(','.join(new_floor))
	return '|'.join(newFloors) + ';' + str(elevator)

def isFloorSafe(floor):
	# If no microchips present then safe (No need to look)
	# If no generators present then safe (No need to look)
	# If all microchips have pair then safe (Could use sum instead of all)			
	
	microChipPairs = [item.replace('M', 'G') in floor for item in floor if item[-1] == 'M']
	return all(pair == microChipPairs[0] for pair in microChipPairs)

""" A* alogorithm approch code
class State:
	def __init__(self, map:object, elevator:int, depth:int) -> None:
		self.map = map
		self.depth = depth
		self.elevator = elevator
		self.hash = hashTheMap(map, elevator)
		self.fit = self.fitness()
	
	def getNewStates(self):
		for movement in [-1, 1]:
			if not 1 <= self.elevator + movement <= 4: continue # Ensure we don't move the elevator off bounds

			currFloor = self.map[self.elevator]
			nextFloor = self.map[self.elevator + movement]
			if self.elevator + movement == 1 and len(nextFloor) == 0: continue # Minor optimization
			# if self.elevator + movement == 2 and len(self.map[1]) == 0 and len(nextFloor) == 0: continue # Minor optimization
			# if self.elevator + movement == 3 and len(self.map[1]) == 0 and len(self.map[2]) == 0 and len(nextFloor) == 0: continue # Minor optimization

			for selectionAmount in [1, 2]:
				if len(currFloor) < selectionAmount: continue
				# Purge all pairs in combinations as they are interchangeable
				for movingItems in combinations(currFloor, selectionAmount):
					pot_currFloor = [item for item in currFloor if item not in movingItems]
					if not isFloorSafe(pot_currFloor): continue
					pot_nextFloor = nextFloor + list(movingItems)
					if not isFloorSafe(pot_nextFloor): continue

					new_map = dict(self.map)
					new_map[self.elevator] = pot_currFloor
					new_map[self.elevator + movement] = pot_nextFloor
					yield State(new_map, self.elevator + movement, self.depth+1)

	
	def fitness(self):
		acc = 0
		for floor, items in enumerate(self.map.values()):
			acc += (4-floor) * len(items)
		return acc
	
	def __lt__(self, other:"State") -> bool:
		return self.fit < other.fit
	
	def __hash__(self) -> int:
		return self.hash
	def __str__(self) -> str:
		return f"Map: [{self.hash}] | Elevator: {self.elevator} | Depth: {self.depth} | Fitness: {self.fit}"
"""

def calcNextMoves(map, elevator, hash):
	# debug = hash == "G&M,G&M,polonium G|G&M,G&M|polonium M|;2"
	# if debug: print('Once upon a time')
	for movement in [-1, 1]:
		if not 1 <= elevator + movement <= 4: continue # Ensure we don't move the elevator off bounds

		currFloor = map[elevator]
		nextFloor = map[elevator + movement]
		if elevator + movement == 1 and len(nextFloor) == 0: continue # Minor optimization
		if elevator + movement == 2 and len(map[1]) == 0 and len(nextFloor) == 0: continue # Minor optimization
		if elevator + movement == 3 and len(map[1]) == 0 and len(map[2]) == 0 and len(nextFloor) == 0: continue # Minor optimization

		for selectionAmount in [1, 2]:
			if len(currFloor) < selectionAmount: continue
			# TODO: Purge all pairs in combinations as they are interchangeable
			for movingItems in combinations(currFloor, selectionAmount):
				pot_currFloor = [item for item in currFloor if item not in movingItems]
				if not isFloorSafe(pot_currFloor): continue
				pot_nextFloor = nextFloor + list(movingItems)
				if not isFloorSafe(pot_nextFloor): continue

				new_map = dict(map)
				new_map[elevator] = pot_currFloor
				new_map[elevator + movement] = pot_nextFloor
				# if debug: print(hashTheMap(new_map, elevator+movement))
				yield {'map': new_map, 'elevator': elevator+movement, 'hash': hashTheMap(new_map, elevator+movement)}

def part1(data):
	itemCount = sum(len(floor) for floor in data.values())
	
	""" A* alogorithm approch code
	queue = [State(data, 1, 0)]
	print(queue[0])
	explored = set()

	while len(queue) > 0:
		instance = heappop(queue)
		# print(instance)
		for new_state in instance.getNewStates():
			if len(new_state.map[4]) == itemCount: print("Found Insane", new_state.depth) # Check for completion
			if new_state.depth > 50: continue # Safe Lock
			if new_state.hash in explored: continue
			explored.add(new_state.hash)
			heappush(queue, new_state)
	
	print(len(explored)) # 1,147,387 but No answer
	"""
			

	steps = 1
	exploreNext = [{'map': data, 'elevator': 1, 'hash': hashTheMap(data, 1)}]
	explored = set(exploreNext[0]['hash'])
	while len(exploreNext) > 0:
		steps += 1
		nextLoop = []
		for situation in exploreNext:
			for new_situation in calcNextMoves(**situation):
				if new_situation['hash'] in explored: continue
				if len(new_situation['map'][4]) == itemCount: return steps-1
				nextLoop.append(new_situation)
				explored.add(new_situation['hash'])
		
		exploreNext = nextLoop
		print(f"Step: {steps} | States Explored: {len(explored)} | States To Be Explored: {len(exploreNext)}")
	# len(explored): v1: 1,576,935 | v2: 1,504,558 (-4.59%) | v3: 1,471,370 (-2.21%)
	


def part2(data):
	data[1].extend(['elerium G', 'elerium M', 'dilithium G', 'dilithium M']) # Expecting 71
	# return part1(data)