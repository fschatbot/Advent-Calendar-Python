split_data = True
completed = False
raw_data = None # Not To be touched

def part1(data):
	counter = 0
	for index, i in enumerate(data[1:]):
		if int(data[index]) < int(i):
			counter += 1
	return counter

def part2(data):
	pass
