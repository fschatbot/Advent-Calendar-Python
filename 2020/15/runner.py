split_data = ','
completed = False
raw_data = None # Not To be touched

def part1(data):
	# Solve day 15 of year 2020 part 1 advent of code
	mem = list(map(int, data))
	for _ in range(2020-len(data)):
		last = mem[-1]
		# Get the indexes of last in mem
		if mem.count(last) == 1:
			mem.append(0)
		else:
			indexes = [i for i, x in enumerate(mem) if x == last]
			mem.append(indexes[-2:][1] - indexes[-2:][0])
	return mem[-1]



def part2(data):
	pass