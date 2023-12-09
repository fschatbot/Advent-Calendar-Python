#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def parse(data):
	numS = re.compile(r'\d+')
	monkeys = {}
	for monk in data.split('\n\n'):
		id, worries, inspMult, testMod, iftrue, iffalse = monk.split('\n')
		monkeys[int(numS.findall(id)[0])] = {
			'worries': [int(worry) for worry in numS.findall(worries)],
			'inspMult': inspMult.split(' = ')[1],
			'testMod': int(numS.findall(testMod)[0]),
			'iftrue': int(numS.findall(iftrue)[0]),
			'iffalse': int(numS.findall(iffalse)[0])
		}
	return monkeys

split_data = parse
completed = 1
raw_data = None # Not To be touched

def part1(data):
	for monk in data: data[monk]['inspected'] = 0 # Adding the inspected meta tag
	for _ in range(20):
		for monk in data:
			monk = data[monk]
			for item in monk['worries']:
				new = eval(monk['inspMult'].replace('old', str(item))) // 3
				data[monk['iftrue' if new % monk['testMod'] == 0 else 'iffalse']]['worries'].append(new)
				monk['inspected'] += 1
			monk['worries'] = []
	
	mostActive = sorted((m['inspected'] for m in data.values()), reverse=True)
	return mostActive[0] * mostActive[1]
	
	

def part2(data):
	# The code is extactly the same as part1
	# TODO: Need to implement the chienese remainder theorem. (Otherwise the digits expand into oblivion)
	for monk in data: data[monk]['inspected'] = 0 # Adding the inspected meta tag
	for _ in range(10_000):
		for monk in data:
			monk = data[monk]
			for item in monk['worries']:
				new = eval(monk['inspMult'].replace('old', str(item)))
				data[monk['iftrue' if new % monk['testMod'] == 0 else 'iffalse']]['worries'].append(new)
				monk['inspected'] += 1
			monk['worries'] = []
	
	mostActive = sorted((m['inspected'] for m in data.values()), reverse=True)
	return mostActive[0] * mostActive[1]