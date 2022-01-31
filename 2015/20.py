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
	num = int(data) / 10
	for i in range( 10_000_000):
		summed = factor_sum(i)
		if summed == num:
			return i
		elif summed > num:
			print("The number is too high", i)
		else:
			print(i, summed,end='\r')

def part2(data):
	pass