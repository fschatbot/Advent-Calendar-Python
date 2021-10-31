split_data = True
raw_data = None # Not To be touched

def part1(data):
	"""The Code is supposed to run here"""
	pass

def part2(data):
	"""The Code is supposed to run here"""
	pass


def main(puzzle_input):
	global raw_data
	raw_data = puzzle_input
	part1(raw_data.split('\n') if split_data else raw_data)
	part2(raw_data.split('\n') if split_data else raw_data)