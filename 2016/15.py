split_data = True
completed = True
raw_data = None # Not To be touched

def process_data(data):
	disks = []
	for line in data:
		line = line.split()
		disks.append((int(line[3]), int(line[11][:-1])))
	return disks

def part1(data):
	disks = process_data(data)

	for time in range(999999999):
		time_index = time
		for disk in disks:
			time_index += 1
			if (time_index + disk[1]) % disk[0] != 0:
				break
		else:
			return time



def part2(data):
	# The code is litteray the same but we add another disk to the list
	disks = process_data(data)
	disks.append((11, 0))

	for time in range(999999999):
		time_index = time
		for disk in disks:
			time_index += 1
			if (time_index + disk[1]) % disk[0] != 0:
				break
		else:
			return time