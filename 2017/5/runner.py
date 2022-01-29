split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	# Convert the data to a list of ints
	ins = list(map(int, data))
	# Create 3 variables
	# -> last_index as None as we havn't started yet. This is to keep track of the curr_index before it changes
	# -> curr_index as 0 as we start at the first index. This is to get the index we are on
	# -> total_step to keep track of the total steps taken
	last_index = None
	curr_index = 0
	total_step = 0
	# We are not using for loop as the curr_index changes based on the data
	while curr_index < len(ins):
		# Change the last index to current index
		last_index = curr_index
		# Add the value to get the new index
		curr_index += ins[curr_index]
		# Increment the last index and total_step by 1
		ins[last_index] += 1
		total_step += 1
	return total_step


def part2(data):
	# This is same as the previous one
	# So half the code is taken from the function above
	ins = list(map(int, data))
	last_index = None
	curr_index = 0
	total_step = 0
	while curr_index < len(ins):
		last_index = curr_index
		curr_index += ins[curr_index]
		# This is for if the value is 3 or bigger we decrese it by 1, else we increase it by 1
		if ins[last_index] >= 3:
			ins[last_index] -= 1
		else:
			ins[last_index] += 1
		total_step += 1
	return total_step