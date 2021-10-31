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
	return mem_len - showcase_len

def part2(data):
	"""The Code is supposed to run here"""
	ori_len = 0
	new_len = 0
	for line in data:
		ori_len += len(line)
		new_len += len(json.dumps(line)) # json dump escapes the string for us.
	return new_len - ori_len