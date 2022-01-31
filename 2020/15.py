split_data = ','
completed = True
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
	mem = list(map(int, data))
	# We create a simple hashmap with all the previous values
	# The hashtable contains the number with the index of it's occurences
	hashmap = {
		x: [i] for i, x in enumerate(mem)
	}
	# Next we loop through the list till 30 million.
	# The i is the index in the mem ;)
	for i in range(len(data), 30_000_000):
		last = mem[-1]
		# Check if only one instance exists
		if len(hashmap[last]) == 1:
			mem.append(0)
			hashmap[0].append(i)
		else:
			# Storing in variable to avoid multiple calculations and lookups
			num = hashmap[last][-1] - hashmap[last][-2]
			mem.append(num)
			# This is done is order to deal we creation of new values
			if num not in hashmap:
				hashmap[num] = [i]
			else:
				hashmap[num].append(i)
		# After each run we add last value to the hashmap with it's index
	# It took me 47.7s and 34.7s to find the answer
	return mem[-1]