split_data = True
completed = False
raw_data = None # Not To be touched

# BTN = Binary To Number
def BTN(binary):
	# Cool trick I found online
	return int(binary, 2)

def part1(data):
	rearranged_data = []
	# We are doing this because we are rearranging the data veritcally than horizontally
	for line in data:
		for index, char in enumerate(line):
			try:
				rearranged_data[index].append(int(char))
			except IndexError:
				rearranged_data.append([int(char)])
	# Now we are going to find which one is more common using the average function
	gamma = ""
	epsilon = ""
	for data in rearranged_data:
		average = sum(data) / len(data)
		# If the average is above 0.5 it means that there are more 1s than 0s
		if average > 0.5:
			gamma += "1"
			epsilon += "0"
		else:
			gamma += "0"
			epsilon += "1"
	return BTN(gamma) * BTN(epsilon)


def part2(data):
	pass