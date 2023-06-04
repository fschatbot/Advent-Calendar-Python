#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = False
completed = True
raw_data = None  # Not To be touched


def part1(data):
	improve_after = int(data)
	scoreboard = "37"
	e1, e2 = 0, 1  # Recipe index of the elfs
	while len(scoreboard) < improve_after+10:
		# Adding the new recipies
		s1 = int(scoreboard[e1])
		s2 = int(scoreboard[e2])
		scoreboard += str(s1 + s2)

		# Moving the elf
		e1 = (e1 + s1 + 1) % len(scoreboard)
		e2 = (e2 + s2 + 1) % len(scoreboard)
	# Return the next 10 digits
	return scoreboard[improve_after:improve_after+11]


def part2(data):
	scoreboard = "37"
	e1, e2 = 0, 1

	# Check at the last plus 1 extra to save computational time
	checkIndex= -len(data) - 1
	while data not in scoreboard[checkIndex:]:
		# Adding the new recipies
		s1 = int(scoreboard[e1])
		s2 = int(scoreboard[e2])
		scoreboard += str(s1 + s2)

		# Moving the elf foward in a cyclic maner
		e1 = (e1 + s1 + 1) % len(scoreboard)
		e2 = (e2 + s2 + 1) % len(scoreboard)
	
	# Now we are simply looking for the index of our data!
	return scoreboard.index(data)
