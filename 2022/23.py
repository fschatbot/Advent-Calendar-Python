#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(data):
	elves = []

	for y, line in enumerate(data.split('\n')):
		for x, chr in enumerate(line):
			if chr != '#': continue
			elves.append((x, y))
	
	return elves

split_data = parse
completed = True
raw_data = None # Not To be touched

def part1(data):
	def empty(check, point):
		return all((point[0]+dx, point[1]+dy) not in data for dx, dy in check)


	north = [(-1, -1), ( 0, -1), ( 1, -1)] # NW, N, NE
	south = [(-1,  1), ( 0,  1), ( 1,  1)] # SW, S, SE
	west  = [(-1, -1), (-1,  0), (-1,  1)] # NW, W, SW
	east  = [( 1, -1), ( 1,  0), ( 1,  1)] # NE, E, SE
	allD  = [(dx, dy) for dy in range(-1, 2) for dx in range(-1, 2) if (dx, dy) != (0, 0)]

	checks = [north, south, west, east]

	for _ in range(10):
		print('Simulation Step:',_+1)
		propositions = {}

		for elve in data:
			if empty(allD, elve): # No move
				propositions[elve] = [elve]
				continue

			for check in checks:
				if empty(check, elve):
					# print(f'Found a valid check for {elve} elve: {check[1]}')
					px, py = elve[0]+check[1][0], elve[1]+check[1][1]
					propositions[(px, py)] = propositions.get((px, py), []) + [elve]
					break
			else:
				propositions[elve] = [elve] # Looks like it had nowhere to move!
		
		checks = checks[1:] + [checks[0]]

		# print(propositions)

		data = []
		for proposed, candiates in propositions.items():
			if len(candiates) == 1:
				data.append(proposed)
			else:
				data.extend(candiates) # Too many elves wishing move to proposed point!
		
		# plotElves(data)
		# if len(data) != 22:
		# 	print("WTF!!")
		# 	print(propositions)
	
	# print(len(data))

	return (max(x for x, y in data) - min(x for x, y in data) + 1) * (max(y for x, y in data) - min(y for x, y in data) + 1) - len(data)

def plotElves(elves):
	minX = min(x for x, y in elves)
	maxX = max(x for x, y in elves) + 1
	minY = min(y for x, y in elves)
	maxY = max(y for x, y in elves) + 1

	for y in range(minY, maxY):
		for x in range(minX, maxX):
			print("#" if (x, y) in elves else ".", end='')
		print()

def part2(data):
	# Took 14.1 minutes but it works
	def empty(check, point):
		return all((point[0]+dx, point[1]+dy) not in data for dx, dy in check)


	north = [(-1, -1), ( 0, -1), ( 1, -1)] # NW, N, NE
	south = [(-1,  1), ( 0,  1), ( 1,  1)] # SW, S, SE
	west  = [(-1, -1), (-1,  0), (-1,  1)] # NW, W, SW
	east  = [( 1, -1), ( 1,  0), ( 1,  1)] # NE, E, SE
	allD  = [(dx, dy) for dy in range(-1, 2) for dx in range(-1, 2) if (dx, dy) != (0, 0)]

	checks = [north, south, west, east]

	i = 0
	while True:
		i += 1
		print('Simulation Step:', i)
		moved = False
		propositions = {}

		for elve in data:
			if empty(allD, elve): # No move
				propositions[elve] = [elve]
				continue
			
			moved = True
			for check in checks:
				if empty(check, elve):
					# print(f'Found a valid check for {elve} elve: {check[1]}')
					px, py = elve[0]+check[1][0], elve[1]+check[1][1]
					propositions[(px, py)] = propositions.get((px, py), []) + [elve]
					break
			else:
				propositions[elve] = [elve] # Looks like it had nowhere to move!
		
		checks = checks[1:] + [checks[0]]

		if not moved:
			break

		# print(propositions)

		data = []
		for proposed, candiates in propositions.items():
			if len(candiates) == 1:
				data.append(proposed)
			else:
				data.extend(candiates) # Too many elves wishing move to proposed point!
		
		# plotElves(data)
		# if len(data) != 22:
		# 	print("WTF!!")
		# 	print(propositions)
	
	# print(len(data))

	return i