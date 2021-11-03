split_data = '\n\n'
completed = True
raw_data = None # Not To be touched

def part1(data):
	total = 0
	for i in data:
		# remove new lines and split each char
		answers = i.replace('\n','')
		# make list of unique chars
		unique_answers = list(set(answers))
		total += len(unique_answers)
	return total

def part2(data):
	total = 0
	for i in data:
		# Go through each char in the first line
		lines = i.split('\n')
		for char in lines[0]:
			# Check if it's there in all the other lines
			if sum(1 for line in lines if char in line) == len(lines):
				total += 1
	return total