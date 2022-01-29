split_data = '\t'
completed = False
raw_data = None # Not To be touched

def part1(data):
	# This creates a list of mem blocks
	data = list(map(int, data))
	# Next create a list and a temp block to see if the block has appeared in the list
	occurances = []
	rect_block = data
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
		
	return len(occurances)

def part2(data):
	pass