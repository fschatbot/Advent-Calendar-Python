import re

split_data = True
completed = False
raw_data = None # Not To be touched

sue_map = []
match_data = {
	'children': 3,
	'cats': 7,
	'samoyeds': 2,
	'pomeranians': 3,
	'akitas': 0,
	'vizslas': 0,
	'goldfish': 5,
	'trees': 3,
	'cars': 2,
	'perfumes': 1
}

def proccess(data):
	for line in data:
		sue_map.append({})
		line = re.sub(r'Sue (\d+): ', '', line) # Remove 'Sue xx: ' from the start
		infos = line.split(', ')
		for info in infos:
			infor = info.split(': ')
			sue_map[-1][infor[0]] = int(infor[1])

def part1(data):
	"""The Code is supposed to run here"""
	proccess(data)
	for index, sue in enumerate(sue_map, start=1):
		for key in sue.keys():
			if sue[key] != match_data[key]:
				break # Not the Sue we wont
		else:
			# If the forloop doesn't break then it means it matched hence it is the Sue that sent us the gift
			return index

def part2(data):
	"""The Code is supposed to run here"""
	# We put functions here to make looking for the thing we want easy
	match_data = {
		'children': 	lambda amount: amount == 3,
		'cats': 		lambda amount: amount > 7,
		'samoyeds': 	lambda amount: amount == 2,
		'pomeranians': 	lambda amount: amount < 3,
		'akitas': 		lambda amount: amount == 0,
		'vizslas': 		lambda amount: amount == 0,
		'goldfish': 	lambda amount: amount < 5,
		'trees': 		lambda amount: amount > 3,
		'cars': 		lambda amount: amount == 2,
		'perfumes': 	lambda amount: amount == 1
	}
	for index, sue in enumerate(sue_map, start=1):
		for key in sue.keys():
			if not match_data[key](sue[key]):
				# We didn't match hence not our aunt sue
				break
		else:
			# The loop didn't break hence it must be our aunt sue
			return index