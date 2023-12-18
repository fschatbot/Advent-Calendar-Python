#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict, Tuple

def parse(data:str):
	data_map = {}
	for y, line in enumerate(data.split('\n')):
		for x, char in enumerate(line):
			if char == '.': continue
			data_map[x, y] = char
	
	return data_map

split_data = parse
completed = True
raw_data = None # Not To be touched

def prettyPrint(data):
	mx, my = max(x[0] for x in data)+1, max(x[1] for x in data)+1
	for y in range(my):
		string = ''
		for x in range(mx):
			string += data.get((x, y), '.')
		print(string)
	print()

def hashString(data):
	mx, my = max(x[0] for x in data)+1, max(x[1] for x in data)+1
	final = []
	for y in range(my):
		string = ''
		for x in range(mx):
			string += data.get((x, y), '.')
		final.append(string)
	return '\n'.join(final)

def part1(data:Dict[Tuple[int, int], str]):
	mx, my = max(x[0] for x in data)+1, max(x[1] for x in data)+1
	# print(f'Map Size: {mx, my}')

	for y in range(my):
		for x in range(mx):
			if data.get((x, y), '.') != 'O': continue
			ny = y
			while 0 < ny and (x, ny-1) not in data:
				ny -= 1
			if y != ny:
				data[x, ny] = 'O'
				del data[x, y]

	return sum(my-p[1] for p,i in data.items() if i == 'O')		


def part2(data:Dict[Tuple[int, int], str]):
	mx, my = max(x[0] for x in data)+1, max(x[1] for x in data)+1
	# print(f'Map Size: {mx, my}')

	# print('Original:')
	# prettyPrint(data)

	seen = []

	for i in range(1_000_000_000):

		hashed = hashString(data)
		if hashed in seen:
			final = parse(seen[seen.index(hashed) + ((1_000_000_000 - i) % (len(seen) - seen.index(hashed)))])
			return sum(my-p[1] for p,i in final.items() if i == 'O')
		else:
			seen.append(hashString(data))
		
		# Everything BELOW WORKS AS INTENDED. ITS THE ABOVE PART WHICH IS BROKEN!

		for y in range(my):
			for x in range(mx):
				if data.get((x, y), '.') != 'O': continue
				ny = y
				while 0 < ny and (x, ny-1) not in data:
					ny -= 1
				if y != ny:
					data[x, ny] = 'O'
					del data[x, y]
		
		# print('North:')
		# prettyPrint(data)
		
		for x in range(mx):
			for y in range(my):
				if data.get((x, y), '.') != 'O': continue
				nx = x
				while 0 < nx and (nx-1, y) not in data:
					nx -= 1
				if x != nx:
					data[nx, y] = 'O'
					del data[x, y]
		
		# print('West:')
		# prettyPrint(data)
		
		for y in range(my, -1, -1):
			for x in range(mx):
				if data.get((x, y), '.') != 'O': continue
				ny = y
				while ny < my-1 and (x, ny+1) not in data:
					ny += 1
				if y != ny:
					data[x, ny] = 'O'
					del data[x, y]

		# print('South:')
		# prettyPrint(data)
		
		for x in range(mx, -1, -1):
			for y in range(my):
				if data.get((x, y), '.') != 'O': continue
				nx = x
				while nx < mx-1 and (nx+1, y) not in data:
					nx += 1
				if x != nx:
					data[nx, y] = 'O'
					del data[x, y]
		
		# print('East:')
		# prettyPrint(data)
		
		
					
		

	return sum(my-p[1] for p,i in data.items() if i == 'O')		