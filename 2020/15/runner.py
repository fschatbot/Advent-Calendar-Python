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
	# Expecting a 7
	mem = list(map(int, data))
	hashmap = {
		x: [i] for i, x in enumerate(mem)
	}
	for i in range(len(data), 30_000_000):
		last = mem[-1]
		if len(hashmap[last]) == 1:
			mem.append(0)
			hashmap[0].append(i)
		else:
			num = hashmap[last][-1] - hashmap[last][-2]
			mem.append(num)
			if num not in hashmap:
				hashmap[num] = [i]
			else:
				hashmap[num].append(i)
	return mem[-1]