#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import heappop, heappush


def parse(data):
	available, required = data.split('\n\n')
	available = available.split(', ')
	required = required.split('\n')

	return available, required

split_data = parse
completed = True
raw_data = None # Not To be touched

def Astar(design:str, available):
	queue = [len(design)] # heuristic, unique number
	while len(queue) > 0:
		lenRemaining = heappop(queue)

		for avail in available:
			if not design[-lenRemaining:].startswith(avail): continue
			if lenRemaining - len(avail) == 0: return True
			heappush(queue, lenRemaining-len(avail))
	
	return False

def part1(data):
	available, required = data

	cummilation = 0
	
	for design in required:
		cummilation += int(Astar(design, available)) # True/False -> 1/0
	return cummilation

def possibilityFinder(design:str, available):
	queue = {len(design): 1}

	for i in range(len(design), 0, -1):
		if not queue.get(i): continue

		for avail in available:
			if not design[-i:].startswith(avail): continue
			queue[i-len(avail)] = queue.get(i-len(avail), 0) + queue[i]
	
	return queue.get(0, 0)

def part2(data):
	available, required = data

	cummilation = 0
	
	for design in required:
		cummilation += possibilityFinder(design, available)
	return cummilation