import re
split_data = False
completed = True
raw_data = None # Not To be touched

def part1(data):
	"""The Code is supposed to run here"""
	final_str = data
	for _ in range(40):
		new_str = ''
		# This regex was compiled using MaxArt2501 help. Check his github page out
		# The (\d) is just making a group of the selected number
		# \1* looks for the group's number further and adds it to the match
		# .finditer is being used to look for this regex allover the string and makes sure that they don't overlap
		result = re.finditer(r'(\d)\1*', final_str)
		for i in result:
			new_str += f'{len(i.group())}{i.group()[0]}'
		final_str = new_str
	return len(final_str)

def part2(data):
	"""The Code is supposed to run here"""
	final_str = data
	for _ in range(50):
		new_str = ''
		result = re.finditer(r'(\d)\1*', final_str)
		for i in result:
			new_str += f'{len(i.group())}{i.group()[0]}'
		final_str = new_str
	return len(final_str)