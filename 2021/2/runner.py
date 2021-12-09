split_data = True
completed = False
raw_data = None # Not To be touched

def part1(data):
	dept = 0
	forward = 0
	for line in data:
		command,amount = line.split()
		if command == "forward":
			forward += int(amount)
		elif command == "down":
			dept += int(amount)
		elif command == "up":
			dept -= int(amount)
	return dept * forward


def part2(data):
	pass