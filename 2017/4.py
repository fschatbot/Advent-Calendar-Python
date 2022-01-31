split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	# Define a valid counter and loop through the data
	vaid = 0
	for line in data:
		# Split the line from spaces
		line = line.split()
		# set() reomoves any duplicate
		# Next we comapare the previous and the next with len() to see if they are the same
		if len(line) == len(set(line)):
			# Increment the valid counter
			vaid += 1
	return vaid

def part2(data):
	valid = 0
	for line in data:
		# We create a dummy new_line to hold the other letters
		line = line.split()
		new_line = []
		for word in line:
			# Rearranges the chars in a word to alphabeticaly order
			new_word = "".join(sorted([char for char in word]))
			new_line.append(new_word)
		# set() reomoves any duplicate
		# Next we comapare the previous and the next with len() to see if they are the same
		if len(new_line) == len(set(new_line)):
			# Increment the valid counter
			valid += 1
	return valid