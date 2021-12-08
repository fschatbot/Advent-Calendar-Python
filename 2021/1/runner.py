split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	counter = 0
	for index, i in enumerate(data[1:]):
		if int(data[index]) < int(i):
			counter += 1
	return counter

def part2(data):
	data = list(map(int,data))
	# First we create the groups we want
	new_data = []
	for index, _ in enumerate(data[:-2]):
		new_data.append(sum(data[index:index+3]))
	# Now that we have thhe sum of each windows we can now count the increatment
	counter = 0
	for index, i in enumerate(new_data[1:]):
		if new_data[index] < i:
			counter += 1
	return counter

