split_data = False
completed = False
raw_data = None # Not To be touched

def part1(data):
	# Eazy peazy
	return data.count('(') - data.count(')')

def part2(data):
	# A little hard from previous but still easy
	level = 0
	for index, ins in enumerate(data, start=1):
		if ins == '(':
			level += 1
		elif ins == ')':
			level -= 1
		# Check for level being below 0
		if level < 0:
			return index