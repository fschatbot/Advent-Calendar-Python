#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = False
completed = True
raw_data = None # Not To be touched

def part1(data):
	# The way we are going to solve this is we are first going to translate the data into an actual object
	index = 0
	score = 0
	insideGarbage = False # To see if we are inside garbage or not

	dept = 0
	while index < len(data):
		char = data[index]
		# Make sure that the dept is not measured while inside the garbage
		if not insideGarbage and char == '{':
			dept += 1
		elif not insideGarbage and char == '}':
			score += dept # we are escaping the group and hence we increase the score before we exit
			dept -= 1
		elif not insideGarbage and char == '<':
			insideGarbage = True # declare we are inside the garbage
		elif insideGarbage and char == '>':
			insideGarbage = False # exit the garbage
		elif insideGarbage and char == '!':
			index += 1 # This is done to skip the next char
		index += 1
	
	return score
		
def part2(data):
	# This is the samee code as above but minified and comments removed
	index = 0
	score = 0
	insideGarbage = False
	garbageCount = 0

	dept = 0
	while index < len(data):
		char = data[index]
		if not insideGarbage and char == '{': dept += 1
		elif not insideGarbage and char == '}': score += dept; dept -= 1			
		elif not insideGarbage and char == '<': insideGarbage = True
		elif insideGarbage and char == '>': insideGarbage = False
		elif insideGarbage and char == '!': index += 1
		elif insideGarbage:
			# Because ! skipping is done above only the garbage characters are counted
			garbageCount += 1 
		index += 1
	
	return garbageCount