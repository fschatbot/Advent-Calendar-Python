from hashlib import md5
from functools import lru_cache
import re

split_data = False
completed = True
raw_data = None # Not To be touched

@lru_cache(None)
def do_hash(string):
	return md5(string.encode()).hexdigest()

regex = re.compile(r'(.)\1\1')

def part1(data):
	# Creating a hash function like this allows for faster checks
	def hash(x):
		return do_hash(f'{data}{x}')
	
	OTP_count = 0
	for i in range(999999999):
		match = regex.search(hash(i)) # Checking for 3 consecutive characters
		if match:
			lookfor = match.group(1) * 5
			# Check if the lookfor is in any of the next thousand hashes
			for j in range(i+1, i+1001):
				if lookfor in hash(j):
					OTP_count += 1
					# Check if we have the 64th one and if we do, return the index
					if OTP_count == 64:	return i
					break # breaking to for speed


def part2(data):
	# For some reason this part takes 17 minutes to run... I'm not sure why
	def hash(x):
		hashed = do_hash(f'{data}{x}')
		for _ in range(2016): hashed = do_hash(hashed)
		return hashed
	
	OTP_count = 0
	for i in range(999999999):
		match = regex.search(hash(i)) # Checking for 3 consecutive characters
		if match:
			lookfor = match.group(1) * 5
			# Check if the lookfor is in any of the next thousand hashes
			for j in range(i+1, i+1001):
				if lookfor in hash(j):
					OTP_count += 1
					print("OTP Count:", OTP_count, end='\r')
					# Check if we have the 64th one and if we do, return the index
					if OTP_count == 64:	return i
					break # breaking to for speed