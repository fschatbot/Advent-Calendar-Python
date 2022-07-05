#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import deque

split_data = False
completed = True
raw_data = None # Not To be touched

def part1(data):
	players, last_marble = map(int, re.findall(r'(\d+) players; last marble is worth (\d+) points', data)[0])
	circle = [0]
	score = [0] * players
	currI = 0
	for turn in range(last_marble):
		marble = turn + 1
		if marble % 23 == 0:
			score[turn % players] += marble
			currI = (currI - 7) % len(circle)
			score[turn % players] += circle.pop(currI)
		else:
			next2 = (currI + 2) % len(circle)
			# Add the marble between next1 and next2
			currI = next2
			circle.insert(next2, marble)
				
	
	return max(score)

def part2(data):
	# The code is from https://www.reddit.com/r/adventofcode/comments/a4i97s/comment/ebepyc7
	players, last_marble = map(int, re.findall(r'(\d+) players; last marble is worth (\d+) points', data)[0])
	last_marble *= 100 # This is the only difference
	circle = deque([0])
	scores = [0] * players

	for marble in range(1, last_marble+1):
		if marble % 23 == 0:
			circle.rotate(7) # Rotate 7 steps to the left
			scores[marble % players] += marble + circle.pop() # The current marble plus the marble 7 steps to the left
			circle.rotate(-1) # Setting left marble as current marble
		else:
			# This is essentially adding the marble with a marble in the middle
			circle.rotate(-1)
			circle.append(marble)
	
	return max(scores)