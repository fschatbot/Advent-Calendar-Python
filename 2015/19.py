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

def find_all(string, sub):
	# Answer taken from https://stackoverflow.com/a/4664889/13703806
	if string.find(sub) == -1: return []
	start = 0
	while True:
		start = string.find(sub, start)
		if start == -1: return
		yield start
		start += len(sub)

def replace_molecules(molecule, data):
	combinations = []
	for name, replacement in data:
		# Get all the indexes of the replacement in the molecule
		# Answer taken from https://stackoverflow.com/a/4664889/13703806
		indexes = [*find_all(molecule, name)]
		for index in indexes:
			new_molecule = replace_index(molecule, index, name, replacement, 1)
			combinations.append(new_molecule)
	return combinations

def part1(data):
	molecule, replacements  = complile_data(data)
	combinations = replace_molecules(molecule, replacements)
	return len(set(combinations))

def part2(data):
	molecule, replacements  = complile_data(data)
	NotFound = True
	lookfors = ['e']
	steps = 0
	while NotFound:
		steps += 1
		for mole in lookfors:
			combinations = replace_molecules(mole, replacements)
			for combination in combinations:
				if len(combination) > len(molecule):
					continue
				if combination == molecule:
					NotFound = False
				else:
					lookfors.append(combination)
	return steps