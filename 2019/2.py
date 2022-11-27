from .intcode import computer, InvalidOpCode

split_data = ','
completed = True
raw_data = None # Not To be touched


def part1(data):
	# First we do the replacement
	data = list(map(int, data))
	return computer(data, 12, 2)

def part2(data):
	# TODO: COMPLETE THIS
	# Almost same from the previous part, but we need to find the right values
	data = list(map(int, data))

	for noun in range(100):
		for verb in  range(100):
			try: output = computer(data, noun, verb) # <- Coping is important
			except InvalidOpCode: continue

			if output == 19690720:
				return 100 * noun + verb
	
	return "I wonder why it failed... how this is possible !?"