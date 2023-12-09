#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(data):
	template, manual = data.split('\n\n')
	manualDict = {}
	for ins in manual.split('\n'):
		lookfor, insert = ins.split(' -> ')
		manualDict[lookfor] = insert
	return template, manualDict

split_data = parse
completed = True
raw_data = None # Not To be touched

def part1(data):
	comp, manual = data
	step = 0
	while step < 10:
		newComp = ""
		for prev, next in zip(comp[:-1], comp[1:]):
			newComp += prev + manual[prev+next]
		comp = newComp + comp[-1]
		step += 1
	
	high = 0
	low = len(comp)
	for atom in set(comp):
		high = max(high, comp.count(atom))
		low = min(low, comp.count(atom))
	
	return high - low

def part2(data):
	# Instead of simulating the entire expansion and finding what the real atom will look like
	# We are going to simply divide the thing into its overlapping pairs. And do the calculation on the massive scale
	comp, manual = data
	pairs = {p: 0 for p in manual}
	for prev, next in zip(comp[:-1], comp[1:]):
		pairs[prev+next] += 1

	step = 0
	while step < 40:
		new_pairs = {p: 0 for p in manual}
		for k, v in pairs.items():
			if v == 0: continue # Skip calculation if there is no pair ¯\_(ツ)_/¯
			insertion = manual[k]
			new_pairs[k[0] + insertion] += v
			new_pairs[insertion + k[1]] += v
		pairs = new_pairs
		step += 1
	
	# Now we calculate the amount of times. (Tad difficult)
	unique = {x:0 for x in set(a for atom in pairs for a in atom if pairs[atom] != 0)}
	for pair, count in pairs.items():
		unique[pair[0]] += count
		unique[pair[1]] += count
	
	# Letters are being counted twice as they appear twice to form their pairs
	unique = {x: unique[x] // 2 for x in unique}
	 # The first and last letter will always be counted one less due them being on the edge
	unique[comp[0]] += 1
	unique[comp[-1]] += 1

	return unique[max(unique, key=lambda x: unique[x])] - unique[min(unique, key=lambda x: unique[x])]
