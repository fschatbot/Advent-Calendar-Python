#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	safe = 0

	for line in data:
		reports = [int(x) for x in line.split()]
		increasing = True if reports[1] > reports[0] else False
		for r1, r2 in zip(reports[:-1], reports[1:]):
			if increasing and r1 > r2:
				break
			elif not increasing and r1 < r2:
				break
			elif not (1 <= abs(r2 - r1) <= 3):
				break
		else:
			safe += 1
	
	return safe

def part2(data):
	
	safe = 0

	for line in data:
		reports = [int(x) for x in line.split()]
		worked = False
		for i in range(len(line)):
			nreports = reports[:i] + reports[i+1:]
			increasing = True if nreports[1] > nreports[0] else False
			for r1, r2 in zip(nreports[:-1], nreports[1:]):
				if increasing and r1 > r2:
					# print('Broke in increase,', r1, r2)
					break
				elif not increasing and r1 < r2:
					# print('Broke in decrease,', r1, r2)
					break
				elif not (1 <= abs(r2 - r1) <= 3):
					# print('Broke in diff,', r1, r2)
					break
			else:
				worked = True
			
			if worked: break
		
		if worked: safe += 1
				
		
	
	return safe