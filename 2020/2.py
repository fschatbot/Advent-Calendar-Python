import re
split_data = True
completed = True
raw_data = None # Not To be touched

def process(data):
	regx = r'(\d+)-(\d+) (\w): (\w+)'
	new_data = []
	for line in data:
		min, max, char, password = re.fullmatch(regx, line).groups()
		new_data.append({'min':int(min), 'max': int(max), 'char': char, 'password': password})
	return new_data

def part1(data):
	"""The Code is supposed to run here"""
	new_data = process(data)
	count = 0
	for line in new_data:
		if line['password'].count(line['char']) >= line['min'] and line['password'].count(line['char']) <= line['max']:
			count += 1
	return count

def part2(data):
	"""The Code is supposed to run here"""
	new_data = process(data)
	count = 0
	for line in new_data:
		# This looks like an XOR case hence the use of the ^
		if (line['password'][line['min'] - 1] == line['char']) ^ (line['password'][line['max'] - 1] == line['char']):
			count += 1
	return count