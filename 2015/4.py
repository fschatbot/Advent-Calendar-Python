import hashlib

split_data = False
completed = True
raw_data = None # Not To be touched

def part1(key):
	# Go through 10 million hashes to find our baby
	# These will take time as we are brute forcing our way through the hash
	for i in range(10_000_000):
		if hashlib.md5((key + str(i)).encode()).hexdigest()[:5] == '00000':
			return i

def part2(key):
	for i in range(10_000_000):
		if hashlib.md5((key + str(i)).encode()).hexdigest()[:6] == '000000':
			return i