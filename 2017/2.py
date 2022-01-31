import itertools

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	diffs = []
	for line in data:
		# Get all the numbers in the line
		line = list(map(int,line.split('\t')))
		# Add the difference between the largest and smallest number to the list
		diffs.append(max(line) - min(line))
	return sum(diffs)

def part2(data):
	diffs = []
	for line in data:
		# Get all the numbers in the line
		line = list(map(int,line.split('\t')))
		# This creates all the possible combination of numbers
		for item in itertools.permutations(line, 2):
			# Check if the numbers in the line are divisible
			if item[0] % item[1] == 0:
				# If they are, add the quotient to the list
				diffs.append(item[0] // item[1])
				break
	return sum(diffs)