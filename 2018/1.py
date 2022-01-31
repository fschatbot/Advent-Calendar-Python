split_data = True
completed = False
raw_data = None # Not To be touched

def part1(data):
	return sum(map(int, data))

def part2(data, frequency=[0]):
	# TODO: FIX THIS ONE
	return "This one doesn't work please don't use it. Only part 1 works. for now"
	for freq in map(int, data):
		new_freq = frequency[-1] + freq
		if new_freq in frequency:
			return new_freq
		else:
			frequency.append(new_freq)
	else:
		return part2(data, frequency)