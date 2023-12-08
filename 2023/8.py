#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def parse(data):
	data = data.split('\n')
	ins = data[0]
	network = {}
	for line in data[2:]:
		point, nodeIns = line.split(' = ')
		nodeIns = nodeIns[1:-1].split(', ')
		network[point] = nodeIns
	
	return ins, network


split_data = parse
completed = True
raw_data = None # Not To be touched

def part1(data):
	instructions, network = data
	onNode = 'AAA'
	onInsIndex = 0
	steps = 0
	while onNode != 'ZZZ':
		steps += 1
		movement = instructions[onInsIndex % len(instructions)]
		onNode = network[onNode][0 if movement == 'L' else 1]
		onInsIndex += 1
	return steps

def part2(data):
	instructions, network = data
	onNode = [node for node in network if node.endswith('A')]
	firstReach = [None for _ in onNode]
	onInsIndex = 0
	steps = 0
	# All the startNodes will correspond to their Z nodes and will be occur with the same frequency
	# Hence we first calculate the frequncy of their occurance and then we calculate its frequency
	while not all(node.endswith('Z') for node in onNode):
		steps += 1
		movement = instructions[onInsIndex % len(instructions)]
		for i, node in enumerate(onNode):
			if not node.endswith('Z'):
				onNode[i] = network[node][0 if movement == 'L' else 1]
			if onNode[i].endswith('Z') and firstReach[i] == None:
				firstReach[i] = steps
		onInsIndex += 1
	return math.lcm(*firstReach) # Using math.lcm instead of np.lcm.reduce due to math module giving a proper ans