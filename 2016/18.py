split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	rows = data.copy() # It comes in array form by default so we do not need to worry

	def get_tiles(index):
		row = rows[-1]
		def get_index(index):
			if index < 0 or index >= len(row):
				return '.'
			return row[index]
		return get_index(index - 1) + get_index(index) + get_index(index+1)
		

	while len(rows) < 40:
		curr_row = ''
		for index in range(len(rows[-1])):
			tiles = get_tiles(index)
			if tiles in ['^^.', '.^^', '^..', '..^']:
				curr_row += '^'
			else:
				curr_row += '.'
		rows.append(curr_row)
	# Count the number of safe tiles
	safe_tiles = 0
	for row in rows:
		safe_tiles += row.count('.')
	return safe_tiles

def part2(data):
	# Instead of saving all the generated rows in a list and then counting the safe spots
	# We can just count the number of safe spots while generating the row itself
	# This is a much faster, and memory light alternative to the method used above

	row = data[0]
	row_counter = 1
	safe_tiles = 0

	def get_tiles(index):
		def get_index(index):
			if index < 0 or index >= len(row):
				return '.'
			return row[index]
		return get_index(index - 1) + get_index(index) + get_index(index+1)
		

	while row_counter <= 400000:
		curr_row = ''
		for index in range(len(row)):
			tiles = get_tiles(index)
			if tiles in ['^^.', '.^^', '^..', '..^']:
				curr_row += '^'
			else:
				curr_row += '.'
		# Updating the variables
		safe_tiles += row.count('.')
		row = curr_row
		row_counter += 1
	return safe_tiles