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
			line = [int(x) for x in line]
			new_board.append(line)
		new_data['boards'].append(new_board)
	return new_data

split_data = proccess_data
completed = True
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
	# Over here once we get our winner we add it into the winner array(make sure to not repeat)
	# Once all the boards have been added we break the loop and calculate the score based on the last board and number added
	# This way we get the last board and the last number which we use to calulate the score
	# This solution is O(n^2). Even though there are 3 nested for loops, we know that the boards are 5x5 and hence the third loop is also constant


	# Same as above but we calculate all the winners
	drawn = []
	winners = []

	def calculateScore(board, lastNumber):
		unMarkedNumbers = sum(x for line in board for x in line if x not in drawn) # Sum of all the unmarked numbers
		return unMarkedNumbers * lastNumber

	for number in data['nums']:
		# If the amount of winners equal the amount of boards, then it means no more numbers need to be drawn
		if len(winners) == len(data['boards']): break 
		# Mark the number as drawn
		drawn.append(number)
		# Check wheter a board scored or not
		for board in data['boards']:
			if board in winners: continue # If the board is added to the winners then don't waste time here
			for line in board:
				if all(x in drawn for x in line):
					winners.append(board)
					break
			if board in winners: continue # If the board is added to the winners than prevent rare double adding case here...
			for i in range(5):
				if all(line[i] in drawn for line in board):
					winners.append(board)
					break
	
	return calculateScore(winners[-1], drawn[-1])