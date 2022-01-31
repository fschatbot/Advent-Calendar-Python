split_data = '\t'
completed = True
raw_data = None # Not To be touched

def redistribute_until_loop(rect_block):
	occurances = []
	while rect_block not in occurances:
		# If not then append the block in the list
		# we are creating a copy because if we change the rect_block later it will also change the one in the list
		occurances.append(rect_block.copy())
		# Balance the recent block
		# Get the largest block
		# Get the index of the first largest number instance
		# Set the index to 0
		num = max(rect_block)
		index = rect_block.index(num)
		rect_block[index] = 0
		# Distribute the number to the rest of the list
		while num > 0:
			# If there is number to distribute than increase the index
			# Add the 1 to the index and decrease the amount to give
			index = (index + 1) % (len(rect_block))
			rect_block[index] += 1
			num -= 1
	# Now we add the rect_block to the occurances list to be used in part2
	occurances.append(rect_block)
	return occurances

def part1(data):
	# This creates a list of mem blocks
	data = list(map(int, data))
	occurances = redistribute_until_loop(data)
	# We are subtracting 1 because we added an extra for part2
	return len(occurances) - 1

def part2(data):
	data = list(map(int, data))
	occurances = redistribute_until_loop(data)
	# We subtract the index of when the first of the double occuercense was found from the length of the occurances list
	# This gives us the cycles it took for the loop, hence the answer
	return (len(occurances) - 1) - occurances.index(occurances[-1])