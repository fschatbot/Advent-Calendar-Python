import re

split_data = True
completed = False
raw_data = None # Not To be touched

def part1(data):
	nice_strings = 0
	for string in data:
		# Small search for the vowels
		small_search = re.findall(r'(a|e|i|o|u)', string)
		if small_search and len(small_search) >= 3:
			# Medium Search, \w is to look for a letter and \1 is to look for the letter behind it
			if re.search(r'(\w)\1', string):
				# Big Search
				if not any(x in string for x in ['ab', 'cd', 'pq', 'xy']):
					nice_strings += 1
	return nice_strings

def part2(data):
	nice_strings = 0
	for string in data:
		# small search because less work
		if re.search(r'(\w)\w\1', string):
			# medium search because it's a little more complicated
			# (\w\w) creates a group of two characters
			# [\w]* will ignore any characters
			# \1 will look for the first group of two characters
			if re.search(r'(\w\w)[\s\S]*\1', string):
				nice_strings += 1
	return nice_strings