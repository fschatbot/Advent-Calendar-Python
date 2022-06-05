#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

split_data = True
completed = False
raw_data = None # Not To be touched

# This entire function was taken from 2016\23.py and modified
# So If you don't understand it, simply go visit that file

def solve(steps, register):
	index = 0
	output = []

	def getValue(var):
		return register[var] if var in 'abcd' else int(var)
	
	cpy_re = re.compile(r'cpy (-?\d+|[abcd]) ([abcd])')
	inc_re = re.compile(r'inc ([abcd])')
	dec_re = re.compile(r'dec ([abcd])')
	jnz_re = re.compile(r'jnz ([abcd]|-?\d+) ([abcd]|-?\d+)')
	tgl_re = re.compile(r'tgl ([abcd]|-?\d+)')
	out_re = re.compile(r'out ([abcd]|-?\d+)')

	while index < len(steps):
		line = steps[index]

		if cpy_re.match(line):
			if cpy_re.match(line) and inc_re.match(steps[index + 1]) and dec_re.match(steps[index + 2]) and jnz_re.match(steps[index + 3]) and dec_re.match(steps[index + 4]) and jnz_re.match(steps[index + 5]):
				registerToIncrement = inc_re.match(steps[index + 1]).groups()[0]
				supportRegister = dec_re.match(steps[index + 2]).groups()[0]
				first_val = cpy_re.match(line).groups()[0]
				second_val = jnz_re.match(steps[index + 5]).groups()[0]
				register[registerToIncrement] += getValue(first_val) * getValue(second_val)
				register[supportRegister] = 0
				register[second_val] = 0
				index += 6
				continue
			else:
				value, letter = cpy_re.match(line).groups()
				register[letter] = getValue(value)
		elif inc_re.match(line):
			letter = inc_re.match(line).groups()[0]
			register[letter] += 1
		elif dec_re.match(line):
			letter = dec_re.match(line).groups()[0]
			register[letter] -= 1
		elif jnz_re.match(line):
			var, jump = jnz_re.match(line).groups()
			if getValue(var) != 0:
				index += getValue(jump)
				continue
		elif out_re.match(line):
			val = getValue(out_re.match(line).groups()[0])
			output.append(val)

			# A small check to quickly determine if the register is even working
			if output[-1] != (len(output) - 1) % 2:
				return output
			# The code will only be run for the next 100 outputs, after that we will assume the register value to be right
			if len(output) >= 100:
				return output
		elif tgl_re.match(line):
			# We don't need this, but I will still keep it
			var = tgl_re.match(line).groups()[0]
			lineIndex = index + getValue(var)
			if not (0 <= lineIndex < len(steps)):
				pass
			elif len(steps[lineIndex].split()) == 2:
				if steps[lineIndex].startswith('inc'):
					steps[lineIndex] = 'dec' + steps[lineIndex][3:]
				else:
					steps[lineIndex] = 'inc' + steps[lineIndex][3:]
			elif len(steps[lineIndex].split()) == 3:
				
				if steps[lineIndex].startswith('jnz'):
					steps[lineIndex] = 'cpy' + steps[lineIndex][3:]
				else:
					steps[lineIndex] = 'jnz' + steps[lineIndex][3:]

		index += 1
	
	# This is bad
	return output

def part1(data):
	expected = [i % 2 for i in range(100)] # This is what we are expecting as our sample output

	# Sample Register
	register = {
		'a': 0,
		'b': 0,
		'c': 0,
		'd': 0
	}
	while True:
		register['a'] += 1
		if solve(data, register.copy()) == expected:
			return register['a']

def part2(data):
	...