split_data = True
completed = True
raw_data = None # Not To be touched

def proccess_data(data):
	tickets = []
	for ticket in data:
		# Figure out what the ticket row is
		row1, row2 = 0, 127
		for steps in ticket[:-4]:
			if steps == 'F':
				row2 = row2 - round((row2 - row1) / 2)
			elif steps == 'B':
				row1 = row1 + round((row2 - row1) / 2)
		# Figure out what the ticket column is
		col1, col2 = 0, 7
		for steps in ticket[-3:-1]:
			if steps == 'L':
				col2 = col2 - round((col2 - col1) / 2)
			else:
				col1 = col1 + round((col2 - col1) / 2)
		# Final step
		row = row1 if ticket[-4] == 'F' else row2
		col = col1 if ticket[-1] == 'L' else col2
		tickets.append(row * 8 + col)
	return tickets


def part1(data):
	titckets = proccess_data(data)
	return max(titckets)

def part2(data):
	titckets = proccess_data(data)
	# Sort the list and return the missing number
	titckets.sort()
	for i in range(len(titckets)):
		if titckets[i] + 2 == titckets[i+1]:
			return titckets[i] + 1