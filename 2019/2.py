split_data = ','
completed = False
raw_data = None # Not To be touched

def part1(data):
	# First we do the replacement
	data = list(map(int, data))
	data[1] = 12
	data[2] = 2
	# Then we run the program
	i = 0
	while i < len(data):
		if data[i] == 1:
			data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
			i += 4
		elif data[i] == 2:
			data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
			i += 4
		elif data[i] == 99:
			break
		else:
			raise Exception('Invalid opcode')
	return data[0]

def part2(data):
	# TODO: COMPLETE THIS
	# Almost same from the previous part, but we need to find the right values
	data = list(map(int, data))
	data[1] = 12
	data[2] = 2
	# Then we run the program
	i = 0
	while i < len(data):
		if data[i] == 1:
			data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
			i += 4
		elif data[i] == 2:
			data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
			i += 4
		elif data[i] == 99:
			break
		else:
			raise Exception('Invalid opcode')
		if data[0] == 19690720 or data[1] == 19690720:
			return 100 * data[1] + data[2]
	return 100 * data[1] + data[2]