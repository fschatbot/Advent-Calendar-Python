# We use regex for it's overlapping property
import regex as re

split_data = False
completed = True
raw_data = None # Not To be touched

def part1(data):
	# Find all the numbers that repeat twice and match
	# This property is found from https://stackoverflow.com/a/18966891/13703806
	# Ok, so a lot is going in the line below so let me break it down
	# First of all we are using a third party library called regex for it's overlapping property
	# The regex is esetially making a number in a group and then checking if the group occurs
	# The data + data[0] allows us to simulate the circular list
	mathes = re.findall(r'(\d)\1', data+data[0], overlapped=True)
	# Now we are converting the list of strings to a list of ints and then adding them together
	mathes = list(map(int, mathes))
	return sum(mathes)



def part2(data):
	# This time we cannot simply use regex, we need to use a loop
	step = len(data) // 2
	numlist = []
	for i, x in enumerate(data):
		# This allows us to simulate the circular list
		# If the index is greater than the length of the list we wrap back to the start. Simple maths 🤓
		wrap = (i + step) % len(data)
		if x == data[wrap]:
			# Convert it into an integer and add it to the list
			numlist.append(int(x))
	# Return the sum
	return sum(numlist)