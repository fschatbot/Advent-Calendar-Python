split_data = True
completed = True
raw_data = None # Not To be touched

# BTN = Binary To Number
def BTN(binary):
	# Cool trick I found online
	return int(binary, 2)

def part1(data):
	rearranged_data = []
	# We are going to rearrange the data veritcally than horizontally to find common digits
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

def get_common(arr, i):
	# This gets all the 1s and 0s in the same column
	common = [int(string[i]) for string in arr]
	# This is similar to common.count(1) / len(common)
	avr = sum(common) / len(common)
	# So if the average is above 0.5 or 0.5 it means that there are more 1s than 0s
	return ('1', '0') if avr >= 0.5 else ('0', '1')

def part2(data):
	OG = data.copy()
	CS = data.copy()
	for i in range(len(data[0])):
		# Run this if only there are more than one bit left
		if len(OG) != 1:
			# Conduct calculations for oxygen generator rating
			common_int = get_common(OG, i)[0]
			# Filter out all the index that do not have the common integer in the same column
			OG = [string for string in OG if string[i] == common_int]
		# Run this if only there are more than one bit left
		if len(CS) != 1:
			# Conduct calculations for CO2 scrubber rating
			least_common_int = get_common(CS, i)[1]
			# Filter out all the index that do not have the least common integer in the same column
			CS = [string for string in CS if string[i] == least_common_int]
	# The final numbers remaining are the ones that are the ratings
	return BTN(OG[0]) * BTN(CS[0])
