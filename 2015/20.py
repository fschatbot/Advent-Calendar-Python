from math import *
split_data = False
completed = False
raw_data = None # Not To be touched

def factor_sum(num):
	# returns a list of factors of num
	factors = [i+1 for i in range(num) if num % (i+1) == 0]
	return sum(factors)

def part1(data):
	# We wan't to find which house gets the gifts as suggested in the puzzle
	# we will not multiple by 10 to save time, by that I mean very so slithly cause it will take a huge amount of time
	# If you want a faster solution check https://github.com/Peter200lx/advent-of-code/blob/master/2015/day20.py but beaware I didn't understand hence I didn't use it
	num = int(data) // 10
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
	pass