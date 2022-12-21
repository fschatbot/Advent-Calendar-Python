#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	# Parsing the orbit Map to convert them into hashmap
	orbits = {}
	for line in data:
		orbitsto, orbittor = line.split(')')
		orbits[orbittor] = orbitsto
	

	def countOrbit(orbittor):
		"""Counts the amount of orbits till COM form a planet/object"""
		indexOrbitTo = orbits[orbittor]
		counter = 1
		while indexOrbitTo != "COM": # Match the base orbit planet to COM
			counter += 1
			indexOrbitTo = orbits[indexOrbitTo]
		
		return counter
	
	# Adding all the counting
	accumulator = 0
	for planet in orbits:
		accumulator += countOrbit(planet)
	return accumulator

def part2(data):
	# Parsing the orbit Map to convert them into hashmap
	orbits = {}

	for line in data:
		orbitsto, orbittor = line.split(')')
		orbits[orbittor] = orbitsto
	
	# Returns a path from an object to COM
	def orbitPath(orbittor):
		"""Generates an orbit path from the object/planet to COM"""
		indexOrbitTo = orbits[orbittor]
		counter = []
		while indexOrbitTo != "COM": # Match the base orbit planet to COM
			counter.append(indexOrbitTo)
			indexOrbitTo = orbits[indexOrbitTo]
		
		return counter
	
	# Find the planet that is common between you and SAN
	santa = orbitPath('SAN')
	you = orbitPath('YOU')

	FCP = [planet for planet in you if planet in santa][0] # first common planet

	return you.index(FCP) + santa.index(FCP) # Add the distance to FCP to get the orbital jumps required from YOU to SAN