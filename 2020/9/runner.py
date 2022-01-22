split_data = True
completed = False
raw_data = None # Not To be touched

def part1(data):
	# Convert the string to numbers
	data = list(map(int, data))
	# Start looping through the list but start at 26th number
	for i in range(25, len(data)):
		# Get the previous 25 numbers and target number
		numlist = data[i-25:i]
		num = data[i]
		# Loop through the preamble
		for x in numlist:
			# Calc the number required to reach the target number
			lookfor = num - x
			# If the target number is there we break the for loop
			if lookfor in numlist:
				break
		else:
			# If we didn't break the loop we didn't find the two numbers which means this must be the number we are looking for.
			return num

def part2(data):
	pass