#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

# Letters are sorted alphabetically
numberMapping = {
	'abcefg': "0",
	'cf': "1",
	'acdeg': "2",
	'acdfg': "3",
	'bcdf': "4",
	'abdfg': "5",
	'abdefg': "6",
	'acf': "7",
	'abcdefg': "8",
	'abcdfg': "9"
}

def part1(data):
	count = 0
	for line in data:
		_, output = line.split(' | ')
		for char in output.split(' '):
			if len(char) in (2, 4, 3, 7):
				count += 1
	return count

def removeSubString(string, substring):
	# Removes every character in the string that is found in the substring
	return ''.join(char for char in string if char not in substring)

def commons(strings):
	appearance = {char:0 for char in 'abcdefg'}

	for string in strings:
		for char in string:
			appearance[char] += 1
	return [char for char in appearance if appearance[char] == len([*strings])]

def nonCommon(strings):
	appearance = {char:0 for char in 'abcdefg'}

	for string in strings:
		for char in string:
			appearance[char] += 1
	return [char for char in appearance if 0 < appearance[char] < len([*strings])]

def invertWiring(wiring):
	return {input: output for output, input in wiring.items()}

def decode(value, wiring):
	final = ''
	for char in value:
		final += wiring[char]
	
	return ''.join(sorted(char for char in final))

def print_wiring(wiring):
	for output, input in wiring.items():
		print(f'{input} -> {output}')

def part2(data):
	decoded = []
	for line in data:
		wiring = {}
		unique, output = line.split(' | ')
		unique, output = unique.split(' '), output.split(' ')
		# The unique numbers
		one = [case for case in unique if len(case) == 2][0]
		four = [case for case in unique if len(case) == 4][0]
		seven = [case for case in unique if len(case) == 3][0]
		eight = [case for case in unique if len(case) == 7][0]
		
		# Because of 7 and 1 we can tell what a is
		wiring[removeSubString(seven, one)] = 'a'

		# We can guess d and g through commons between 2, 3, 5
		# After which we can remove the "a" wiring.
		dg = commons([case for case in unique if len(case) == 5])
		dg.remove(removeSubString(seven, one)) # removing the "a"
		# Next we can compare the remaining from 0 to get g and which would finalize d
		for case in unique:
			if len(case) != 6: continue # Filter down to 0, 6, 9

			common = commons([case, dg])
			if len(common) > 1: continue # Zero is the one where only one char from dg is present
			wiring[common[0]] = 'g'
			# Remove g from dg to get the remaing d
			dg.remove(common[0])
			wiring[dg[0]] = 'd'
			break

		# We can figure out b by removing commons form 4 and 1 and then remove the d wiring
		wiring[''.join(nonCommon([four, one])).replace(invertWiring(wiring)['d'], '')] = 'b'

		# We can figure out f by looking for commons in 6 letter case and with d (Will Compare 9 and 6)
		f = commons([case for case in unique if len(case) == 6 and invertWiring(wiring)['d'] in case])
		for key in wiring: f.remove(key)
		wiring[f[0]] = 'f'

		# We can figure out c by removing f from one
		c = nonCommon([one, invertWiring(wiring)['f']])[0]
		wiring[c] = 'c'

		# The remaining one will be e
		e = nonCommon(['abcdefg', ''.join(wiring.keys())])[0]
		wiring[e] = 'e'

		finalRead = ''
		for number in output:
			finalRead += numberMapping[decode(number, wiring)]
		decoded.append(int(finalRead))
	
	return sum(decoded)