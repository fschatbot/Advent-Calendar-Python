#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	beams = set([data[0].index('S')])
	counter = 0
	for line in data[1:]:
		new_beams = set()
		for beam in beams:
			if line[beam] == '^':
				new_beams.add(beam-1)
				new_beams.add(beam+1)
				counter += 1
			else:
				new_beams.add(beam)
		beams = new_beams
	return counter


def part2(data):
	beams = {data[0].index('S'): 1}
	for line in data[1:]:
		new_beams = {}
		for beam in beams:
			if line[beam] == '^':
				new_beams[beam-1] = new_beams.get(beam-1, 0) + beams[beam]
				new_beams[beam+1] = new_beams.get(beam+1, 0) + beams[beam]
			else:
				new_beams[beam] = new_beams.get(beam, 0) + beams[beam]
		beams = new_beams
	return sum(beams.values())