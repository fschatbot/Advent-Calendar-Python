#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(data:str):
	# Converts the given data into an tree object
	current = []
	system = {'/': {}}
	folders = []

	for line in data.split('\n'):
		if line == '$ cd ..':
			current.pop()
		elif line.startswith('$ cd'):
			current.append(line[5:])
			folders.append('|'.join(current))
		elif line == '$ ls':
			continue
		elif line.startswith('dir'):
			dir = system
			for nav in current:
				dir = dir[nav]
			dir[line[4:]] = {}
		else:
			dir = system
			for nav in current:
				dir = dir[nav]
			size, name = line.split(' ')
			dir[name] = int(size)
	
	return [system, folders]


split_data = parse
completed = True
raw_data = None # Not To be touched

def calc_size(path, system):
	dir = system
	for nav in path:
		dir = dir[nav]
	
	size = 0
	for name, value in dir.items():
		if type(value) == int:
			size += value
		else:
			size += calc_size(path + [name], system)
	
	return size


def part1(data):
	system, folders = data

	reduced = 0

	for folder in folders:
		size = calc_size(folder.split('|'), system)
		if size <= 100000:
			reduced += size

	return reduced

def part2(data):
	system, folders = data

	unused = 70000000 - calc_size(['/'], system)
	needed = 30000000 - unused
	best = 70000000 # Just need a bigger number that will be reduced slowly

	for folder in folders:
		size = calc_size(folder.split('|'), system)
		if size >= needed:
			best = min(best, size)
	
	return best