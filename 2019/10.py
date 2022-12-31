#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import atan2, degrees, sqrt

split_data = True
completed = True
raw_data = None # Not To be touched

def calcDeg(point1, point2) -> int:
	# degrees(atan2) calculates the bearing of the points
	# The subtraction from 180 just puts the angle in point of the coordinate system followed here
	dx, dy = point2[0] - point1[0], point2[1] - point1[1]
	ang = 180 - degrees(atan2(dx, dy))
	return ang

def calcualteBestStation(astroids:list) -> tuple:
	"""Getting the position and visibility of the place where the astroid should be placed"""
	# Looping through all the astroids
	maxScore = 0
	bestAstro = None
	for x1,y1 in astroids:
		# Making a set of degrees at which an astroid is visible 
		visibleDegrees = set()
		for x2,y2 in astroids:
			if (x1,y1) == (x2, y2): continue
			# Calculating the degrees formed by the 2 points
			dx, dy = x2 - x1, y2 - y1
			visibleDegrees.add(degrees(atan2(dx, dy)))
		# Setting the maxScore and bestAstro value
		if len(visibleDegrees) > maxScore:
			maxScore = len(visibleDegrees)
			bestAstro = (x1, y1)

	return maxScore, bestAstro

def part1(data):
	# Getting coordinates of all astroids
	astroids = []
	for y, line in enumerate(data):
		for x, point in enumerate(line):
			if point == '#': astroids.append((x, y))
	
	visibility, _ = calcualteBestStation(astroids)
	return visibility

def part2(data):
	# Getting coordinates of all astroids
	astroids = []
	for y, line in enumerate(data):
		for x, point in enumerate(line):
			if point == '#': astroids.append((x, y))
	
	# Getting the coordinates of the best station
	_, stationPos = calcualteBestStation(astroids)
	astroids.remove(stationPos) # <- removed as its not an astroid to destroy

	# group each astroid based on degrees and distance from the station
	astroidData = []
	x1, y1 = stationPos
	for x2, y2 in astroids:
		deg = calcDeg((x1, y1), (x2, y2))
		dx, dy = x2 - x1, y2 - y1
		dis = sqrt(dx**2 + dy**2)
		astroidData.append({"x": x2, "y": y2, "degree": deg, "distance": dis})
	
	# Now we custom sort the data

	# sort by degrees
	astroidData.sort(key=lambda a1: a1['degree'])
	# Make a hashmap for degrees and astroids
	astroMap = {}
	for astroid in astroidData:
		if astroid['degree'] not in astroMap: astroMap[astroid['degree']] = []
		astroMap[astroid['degree']].append(astroid)
	# sort each degree by distance
	for deg in astroMap:
		astroMap[deg].sort(key=lambda x: x['distance'])
	# Peel the first of each degree into the flatMap
	flattenedMap = []
	while any(bool(val) for val in astroMap.values()):
		for key in astroMap:
			if not astroMap[key]: continue
			flattenedMap.append(astroMap[key].pop(0))
	
	# Return Value
	return flattenedMap[199]['x'] * 100 + flattenedMap[199]['y']