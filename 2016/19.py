from math import log, floor

split_data = False
completed = True
raw_data = None # Not To be touched

def part1(data):
	# This sum could be easily solved using the trick shown in the video. https://www.youtube.com/watch?v=uCsD3ZGzMgE
	return int('0b' + bin(int(data))[3:] + '1', 2)

def part2(data):
	# I was heavily inspired from https://www.reddit.com/r/adventofcode/comments/5j4lp1/comment/dbdf50n
	# However I will try and break this down

	# If you do this problem with 'n' number. You would notice that 3^a + 1 are always 1.
	# We also notice that any number after that is just increasing by 1.
	# If we look at the corelation, we can see that ans the largest power of 3 possbile subtracted from the target

	# We can get the largest power of 3 by taking the floor of log(target) with base 3
	# Next we simply subtract the answer from the target

	target = int(data)
	return target - 3 ** floor(log(target, 3))