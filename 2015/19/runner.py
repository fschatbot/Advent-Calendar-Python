import re

split_data = '\n'
completed = False
raw_data = None # Not To be touched

def complile_data(data):
	# A Simple Compliler
	# Get the molecule data and replace ment is also pretty simple
	return data[-1], [x.split(' => ') for x in data[:-2]]

def replace_index(string, index, old_str, new_str, count):
	return string[:index] + string[index:].replace(old_str, new_str, count)

def part1(data):
	molecule, replacements  = complile_data(data)
	combinations = []
	for name, replacement in replacements:
		# Get all the indexes of the replacement in the molecule
		# Answer taken from https://stackoverflow.com/a/4664889/13703806
		indexes = [m.start() for m in re.finditer(name, molecule)]
		for index in indexes:
			new_molecule = replace_index(molecule, index, name, replacement, 1)
			combinations.append(new_molecule)
	return len(set(combinations))

def part2(data):
	pass