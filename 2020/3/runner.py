split_data = True
completed = False
raw_data = None # Not To be touched

def part1(data, right=3, down=1):
	pos = 0
	encounters = 0
	for index in range(0, len(data), down):
		line = data[index]
		wrap = pos % len(line)
		pos += right
		if line[wrap] == '#':
			encounters += 1
	return encounters


def part2(data):
	# This is a bit of a hack, but it works
	enc1 = part1(data, 1)
	enc2 = part1(data, 3)
	enc3 = part1(data, 5)
	enc4 = part1(data, 7)
	enc5 = part1(data, 1, 2)
	return enc1 * enc2 * enc3 * enc4 * enc5