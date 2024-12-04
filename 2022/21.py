#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(data):
	monkeys = {}

	for monkey in data.split('\n'):
		name, operation = monkey.split(': ')
		if any(op in operation for op in '+-/*'):
			monkeys[name] = operation.split(' ')
		else:
			monkeys[name] = int(operation)
	
	return monkeys

split_data = parse
completed = True
raw_data = None # Not To be touched

def part1(data):
	def get_monkey(name):
		yells = data[name]
		if isinstance(yells, int): return yells
		mon1 = get_monkey(yells[0])
		mon2 = get_monkey(yells[2])

		match yells[1]:
			case '+':
				return mon1 + mon2
			case '-':
				return mon1 - mon2
			case '*':
				return mon1 * mon2
			case '/':
				return mon1 // mon2
	
	return get_monkey('root')


def part2(data):
	# Inbuilt complex number class to the rescue!
	data['root'][1] = '='
	
	def get_monkey(name):
		if name == 'humn':
			return complex(0, 1)
		yells = data[name]
		if isinstance(yells, int): return yells
		mon1 = get_monkey(yells[0])
		mon2 = get_monkey(yells[2])

		match yells[1]:
			case '+':
				return mon1 + mon2
			case '-':
				return mon1 - mon2
			case '*':
				return mon1 * mon2
			case '/':
				return mon1 / mon2
			case '=':
				return mon1, mon2
	
	out1, out2 = get_monkey('root')
	comp, norm = (out1, out2) if isinstance(out1, complex) else (out2, out1)

	# This ends give the following algebra equation:
	# comp.real + comp.imag * x = norm

	return int((norm - comp.real) // comp.imag) # A bit of algebra