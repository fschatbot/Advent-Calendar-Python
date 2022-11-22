#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = 1
raw_data = None # Not To be touched

def part1(data):
	# Processing the data and making a hashmap out of it
	communication_map = {}
	for line in data:
		program, connection = line.split(' <-> ')
		communication_map[program] = connection.split(', ')
	
	counter = 0
	for program in communication_map:
		# This is a basic communication path builder
		# Programs in look for are the one's whose connnections will be explored
		# looked at variable make sure that we don't look at the same connection twice
		lookedat = []
		lookfor = communication_map[program]
		# If we have connections to look for executee the program
		while lookfor:
			# if lookfor is not empty, shift the lookfor list to lookedat and add the new programs that we will be looking at
			temp = []
			for prog in lookfor:
				if prog in lookedat:continue
				temp.extend(communication_map[prog])
			lookedat = list(set(lookedat + lookfor))
			lookfor = list(set(temp))
		if '0' in lookedat:
			counter += 1
	
	return counter

def part2(data):
	...