split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	col = [[] for _ in range(len(data[0]))]
	# Convert row to column
	for line in data:
		for j in range(len(line)):
			col[j].append(line[j])
	# Find the most common letter in each column
	for index, line in enumerate(col):
		col[index] = max(line, key=line.count)
	return ''.join(col)


def part2(data):
	col = [[] for _ in range(len(data[0]))]
	# Convert row to column
	for line in data:
		for j in range(len(line)):
			col[j].append(line[j])
	# Find the least common letter in each column
	for index, line in enumerate(col):
		col[index] = min(line, key=line.count)
	return ''.join(col)