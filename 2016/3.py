import re

split_data = '\n' # Doing this to strip each line by default
completed = True
raw_data = None # Not To be touched

def part1(data):
	possible = 0
	for line in data:
		# This will get all the numbers and sort them from smallest to largest
		nums = sorted(int(x) for x in re.split(r'\s+', line))
		# Next to validate triangles, the smaller 2 sides must be greater than the larger side
		if nums[0] + nums[1] > nums[2]:
			possible += 1
	return possible

def part2(data):
	# We simply have to rearrange the given data to solve this part
	# Converting the rows to columns
	new_data = [[], [], []]
	for line in data:
		nums = re.split(r'\s+', line)
		for i in range(3):
			new_data[i].append(int(nums[i])) 
	# Flattening the list
	new_data = [x for y in new_data for x in y] # IDK how this works but it does
	# Now we can chunk the list so we can have lists of sides
	chunks = [new_data[i:i+3] for i in range(0, len(new_data), 3)]
	# Now we can validate the triangles
	possible = 0
	for chunk in chunks:
		# This will get all the numbers and sort them from smallest to largest
		nums = sorted(chunk)
		# Next to validate triangles, the smaller 2 sides must be greater than the larger side
		if nums[0] + nums[1] > nums[2]:
			possible += 1
	return possible
