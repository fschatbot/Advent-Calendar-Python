import itertools

split_data = True
completed = False
raw_data = None # Not To be touched

def part1(data):
	"""The Code is supposed to run here"""
	data = list(map(int, data))
	for a in data:
		for b in data:
			if a + b == 2020:
				return a * b

def part2(data):
	"""The Code is supposed to run here"""
	data = list(map(int, data))
	for a in data:
		for b in data:
			for c in data:
				if a + b + c == 2020:
					return a * b * c