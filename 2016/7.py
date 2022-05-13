import re

split_data = True
completed = False
raw_data = None # Not To be touched

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


def part2(data):
	pass