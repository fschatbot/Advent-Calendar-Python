import json

split_data = False
completed = True
raw_data = None # Not To be touched

def loop1(data):
	total = 0
	if isinstance(data, int):
		return data
	elif isinstance(data, str):
		return 0
	elif isinstance(data, list):
		for i in data:
			if isinstance(i, (list, object)):
				total += loop1(i)
			elif isinstance(i, int):
				total += i
	elif isinstance(data, object):
		for i in data.values():
			if isinstance(i, (list, object)):
				total += loop1(i)
			elif isinstance(i, int):
				total += i
	return total

def loop2(data):
	total = 0
	if isinstance(data, int):
		return data
	elif isinstance(data, str):
		return 0
	elif isinstance(data, list):
		for i in data:
			if isinstance(i, (list, object)):
				total += loop2(i)
			elif isinstance(i, int):
				total += i
	elif isinstance(data, object):
		if 'red' in data.values() or 'red' in data.keys():
			return 0
		for i in data.values():
			if isinstance(i, (list, object)):
				total += loop2(i)
			elif isinstance(i, int):
				total += i
	return total

def part1(data):
	"""The Code is supposed to run here"""
	data = json.loads(data)
	return loop1(data)

def part2(data):
	"""The Code is supposed to run here"""
	data = json.loads(data)
	return loop2(data)