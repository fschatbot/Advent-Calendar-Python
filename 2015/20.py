split_data = int
completed = True
raw_data = None # Not To be touched

def factor_sum(num):
	# returns a list of factors of num
	factors = [i+1 for i in range(num) if num % (i+1) == 0]
	return sum(factors)

def part1(data):
	num = data // 10
	# We are just going to keep on delivering presents to each house until we get to the house we are looking for
	houses = [0] * num
	# Loop Through Each Number
	for i in range(1, num):
		# Loop through all the houses that this number is going to visit and deliver the present
		# Starting from i-1 because we need to take 0 in account
		for j in range(i-1, num, i):
			houses[j] += i
	# Check for which house has the number we are looking for
	for index, house in enumerate(houses):
		# ok we need to see which house have "ATLEAST" the number of presents we are looking for, instead of which house has "EXACTLY" the number of presents
		if house >= num:
			return index + 1

def part2(data):
	# The code in part2 is copied from part1
	# Dividing by 11 and not 10 because we deliver 11 presents each time and not 10
	num = data // 11
	houses = [0] * num
	for i in range(1, num):
		# Make a counter to keep track of the number of times a present is delivered
		counter = 0
		for j in range(i-1, num, i):
			# Simple check to see if the counter is not above 50
			if counter > 50: break
			# Deliver the present and increment the counter
			houses[j] += i * 11
			counter += 1
	for index, house in enumerate(houses):
		if house >= data:
			return index + 1
