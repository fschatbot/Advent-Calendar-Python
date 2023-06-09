#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

closeMap = {
	')': '(',
	']': '[',
	'}': '{',
	'>': '<'
}

def part1(data):
	scoreSystem = {
		')': 3,
		']': 57,
		'}': 1197,
		'>': 25137
	}

	score = 0
	for line in data:
		tracker = ''
		for char in line:
			if char not in closeMap:
				tracker += char
			elif tracker[-1] == closeMap[char]:
				tracker = tracker[:-1]
			else:
				score += scoreSystem[char]
				break
	return score

def part2(data):
	scoreSystem = {
		'(': 1,
		'[': 2,
		'{': 3,
		'<': 4
	}

	scores = []
	for line in data:
		tracker = ''
		for char in line:
			if char not in closeMap:
				tracker += char
			elif tracker[-1] == closeMap[char]:
				tracker = tracker[:-1]
			else:
				# Corrupt line
				break
		else:
			# This would not run if the break is not executed
			# Looking for incomplete lines
			if tracker != '':
				lineScore = 0
				for char in tracker[::-1]:
					lineScore = lineScore * 5 + scoreSystem[char]
				scores.append(lineScore)
	
	return sorted(scores)[len(scores) // 2]