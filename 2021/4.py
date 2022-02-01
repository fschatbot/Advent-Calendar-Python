def proccess_data(data):
	data = data.split('\n\n')
	new_data = {}
	# This gets all the numbers which are going to be drawn
	new_data['nums'] = list(map(int, data[0].split(',')))
	# This gets all the boards
	new_data['boards'] = []
	for board in data[1:]:
		board = board.replace('  ', ' ')
		# Go through each line and create an array of the ints on the line
		new_board = []
		for line in board.split('\n'):
			line = line.strip().split()
			# This shows the number and wheter it has been marked or not
			line = [(int(x), False) for x in line]
			new_board.append(line)
		new_data['boards'].append(new_board)
	return new_data

split_data = proccess_data
completed = False
raw_data = None # Not To be touched

def part1(data):
	print(data)

def part2(data):
	pass