#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	head = [0, 0]
	tail = [0, 0]
	visits = set()

	def updateTail():
		# If the x and y are within ±1 distance then its fine
		while not all(abs(h - t) <= 1 for h, t in zip(head, tail)):
			if head[0] != tail[0]:
				tail[0] += 1 if head[0] > tail[0] else -1
			if head[1] != tail[1]:
				tail[1] += 1 if head[1] > tail[1] else -1
	
	moveMap = {
		'L': (-1,  0),
		'R': (+1,  0),
		'U': ( 0, -1),
		'D': ( 0, +1)
	}
	for line in data:
		ins, count = line.split(' ')
		dx, dy = moveMap[ins]
		for _ in range(int(count)):
			head[0] += dx
			head[1] += dy
			updateTail()
			visits.add(','.join(map(str, tail)))

	return len(visits)

def part2(data):
	knots = [[0, 0] for _ in range(10)]
	visits = set()

	def updateKnot(head, tail):
		# If the x and y are within ±1 distance then its fine
		while not all(abs(h - t) <= 1 for h, t in zip(head, tail)):
			if head[0] != tail[0]:
				tail[0] += 1 if head[0] > tail[0] else -1
			if head[1] != tail[1]:
				tail[1] += 1 if head[1] > tail[1] else -1
		return tail
	
	moveMap = {
		'L': (-1,  0),
		'R': (+1,  0),
		'U': ( 0, -1),
		'D': ( 0, +1)
	}
	for line in data:
		ins, count = line.split(' ')
		dx, dy = moveMap[ins]
		for _ in range(int(count)):
			knots[0][0] += dx
			knots[0][1] += dy
			for headKnot, tailKnot in zip(knots[:-1], knots[1:]):
				tailKnot = updateKnot(headKnot, tailKnot)
			visits.add(','.join(map(str, knots[-1])))
	
	return len(visits)