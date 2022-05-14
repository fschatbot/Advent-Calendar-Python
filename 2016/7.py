import regex # we will use third party regex library in order to get overlapping regex matches
import re

split_data = True
completed = True
raw_data = None # Not To be touched

# I really needed help from https://github.com/natemago/adventofcode2016/ in order to complete this day
# This day was somewhat not clear and regex sometimes wanted to work and sometimes not...

def part1(data):
	supported = 0
	for line in data:
		# (\w) makes group with letter
		# (?!\1) makes sure that the first group has not been repeated
		# (\w+) makes another group with letter another letter
		# \2\1 makes sure that the groups reppear but not in the same order
		# This regex elimniates the possibility of 'aaaa' being matched
		# 'aaaa' being matched was supported then the pattern (.)(.)\2\1 would have worked
		if re.search(r'(\w)(?!\1)(\w)\2\1', line):
			# Here is a small thing that advent of code didn't tell us
			# IF ABBA is in the hypernet, it's not a valid IP even if another ABBA is in the supernet
			# So the next if statement checks if another 'abba' instance is there in the hypernet			
			if not re.search(
				r'\[[^\]]*' + # Checks for opening bracket and anything inside it (except the closing bracket)
				r'(\w)(?!\1)(\w)\2\1' + # Checks for the abba pattern
				r'[^\]]*\]' # Checks for the closing bracket
				, line):
				supported += 1
	return supported



def isLineSupported(line):
	# Split the data to get all the supernets aka (the part not in brackets)
	# re.split has not be used because it would capture the content inside the brackets aswell
	supernets = re.sub(r'\[(\w+)\]','|',line).split('|')
	# Search for aba patterns in the supernets
	for supernet in supernets:
		match = regex.findall(r'(\w)(?!\1)(\w)\1', supernet, overlapped=True) # find all overlapping aba patterns
		if not match: continue # Check if any matches were found
		babs = [aba[1] + aba[0] + aba[1] for aba in match] # If yes, convert the matches into bab patterns
		for bab in babs:
			# Loop through all the bab patterns and check if any are there in any hypernets
			for hypernet in re.finditer(r'\[(\w+)\]', line):
				if bab in hypernet.group(1): # If yes, return True because the IP is valid
					return True

def part2(data):
	# A simple counter for all the times the IP is valid
	return sum(1 for line in data if isLineSupported(line))