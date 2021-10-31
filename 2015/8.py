import json

split_data = True
raw_data = None # Not To be touched

def part1(data):
	"""The Code is supposed to run here"""
	mem_len = 0
	showcase_len = 0
	for line in data:
		mem_len += len(line)
		new_str = eval(line)
		showcase_len += len(new_str)
	print("Answer To the First Part:", mem_len - showcase_len)

def part2(data):
	"""The Code is supposed to run here"""
	def str_to_raw(string):
		# raw_map = {8:r'\b', 7:r'\a', 12:r'\f', 10:r'\n', 13:r'\r', 9:r'\t', 11:r'\v'}
		return r''.join(char for char in string)
	ori_len = 0
	new_len = 0
	for line in data:
		ori_len += len(line)
		new_len += len(json.dumps(line)) # json dump escapes the string for us.
	print("Answer To the Second Part:", new_len - ori_len)


def main(puzzle_input):
	global raw_data
	raw_data = puzzle_input
	part1(raw_data.split('\n') if split_data else raw_data)
	part2(raw_data.split('\n') if split_data else raw_data)