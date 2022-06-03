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

	# We simply need the largest power of 3 that is less than the target
	# Taking a log of the target might will fail if the target is a power of 3

	target = int(data)
	i = 1

	while i * 3 < target:
		i *= 3

	return target - i

