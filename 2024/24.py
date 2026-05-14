#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(data):
	wires = {}

	section_1, section_2 = data.strip().split('\n\n')
	for line in section_1.split('\n'):
		wire, output = line.split(': ')
		wires[wire] = int(output)
	
	queue = []

	for line in section_2.split('\n'):
		inp_1, op, inp_2, _, wire = line.split()
		wires[wire] = [inp_1, inp_2, op]
		if wire[0] == 'z':
			queue.append(wire)
	
	return wires, queue

split_data = parse
completed = 1
raw_data = None # Not To be touched

def part1(data):
	wires, z_wires = data

	def determine(wire):
		if type(wires[wire]) == int:
			return wires[wire]
		inp_1, inp_2, op = wires[wire]
		inp_1 = determine(inp_1)
		inp_2 = determine(inp_2)
		if op == 'AND':
			out = inp_1 & inp_2
		elif op == 'OR':
			out = inp_1 | inp_2
		else:
			out = inp_1 ^ inp_2
		wires[wire] = out
		return out
	
	number = ''.join(str(determine(wire)) for wire in sorted(z_wires, reverse=True))
	print(number)
	return int(number, 2)
		

def part2(data):
	# We need to study a total of 8 eight swaps. Going based on combinatorics that is 221!/(213)! ~= 2*10^16
	# So we need to come up with a smarted way. We know that the operations are supposed to perform addition
	# We also know they start with x## and y## and we perform addition.

	# Since we know it is addition. We can start by matching the least significant bits...
	# Their mistake can tell us which section the fault lies in, which section it doesn't and so on...

	# We could even try and compare the wiring presented to the actual bit adder diagrams and go from there
	



	wires, z_wires = data
	x_wires = sorted([wire for wire in wires if wire[0] == 'x'], reverse=True)
	y_wires = sorted([wire for wire in wires if wire[0] == 'y'], reverse=True)
	x_number = int(''.join(str(wires[wire]) for wire in x_wires), 2)
	y_number = int(''.join(str(wires[wire]) for wire in y_wires), 2)

	print(''.join(str(wires[wire]) for wire in x_wires))
	print(''.join(str(wires[wire]) for wire in y_wires))
	print(bin(x_number+y_number)[2:])

	print(x_number, y_number, x_number + y_number)


	# Get me all the x and y wires...
	...