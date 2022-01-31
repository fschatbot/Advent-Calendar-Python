split_data = True
completed = True
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
	# We get our target number
	target = part1(data)
	# Convert the string to numbers
	data = list(map(int, data))
	# The time for required for the solution is O(n^2) for 0.3s
	# First we loop through all the possible list combinations
	for i,_ in enumerate(data):
		# The i+1 makes the list loop get smaller and faster
		for j in range(i+1, len(data)):
			# Get the sum of the range
			setsum = sum(data[i:j])
			# This saves us time from the list being denied from 2 checks
			if setsum < target:
				continue
			# This saves us a lot of time as it cancels out i as the possible number
			elif setsum > target:
				break
			# We got out set
			elif setsum == target:
				# We could use sorting but why waste time
				# use min to get the smallest number and max to get the largest number
				return min(data[i:j]) + max(data[i:j])