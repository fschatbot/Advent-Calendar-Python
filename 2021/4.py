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
			line = [int(x) for x in line]
			new_board.append(line)
		new_data['boards'].append(new_board)
	return new_data

split_data = proccess_data
completed = 1
raw_data = None # Not To be touched

def part1(data):
	drawn = []

	def calculateScore(board, lastNumber):
		unMarkedNumbers = sum(x for line in board for x in line if x not in drawn) # Sum of all the unmarked numbers
		return unMarkedNumbers * lastNumber

	for number in data['nums']:
		# Mark the number as drawn
		drawn.append(number)
		# Check wheter a board scored or not
		for board in data['boards']:
			for line in board:
				if all(x in drawn for x in line):
					return calculateScore(board, number)
			for i in range(5):
				if all(line[i] in drawn for line in board):
					return calculateScore(board, number)

def part2(data):
	pass