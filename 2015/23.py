split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	# Defines two variables a and b with the value of 0
	a = b = 0
	i = 0
	while i < len(data):
		line = data[i]
		if line.startswith('hlf'):
			if line.endswith('a'):
				a /= 2
			else:
				b /= 2
		elif line.startswith('tpl'):
			if line.endswith('a'):
				a *= 3
			else:
				b *= 3
		elif line.startswith('inc'):
			if line.endswith('a'):
				a += 1
			else:
				b += 1
		elif line.startswith('jmp'):
			i += int(line[4:])
			continue
		elif line.startswith('jie'):
			if line.split(',')[0].endswith('a'):
				if a % 2 == 0:
					i += int(line.split(',')[1])
					continue
			else:
				if b % 2 == 0:
					i += int(line.split(',')[1])
					continue
		elif line.startswith('jio'):
			# Common Error People Made is that jio is "jump if ONE" and not odd
			if line.split(',')[0].endswith('a'):
				if a == 1:
					i += int(line.split(',')[1])
					continue
			else:
				if b == 1:
					i += int(line.split(',')[1])
					continue
		i += 1
	return b

def part2(data):
	# Copy paste the code from part one and tweak it a bit
	a = 1
	b = 0
	i = 0
	while i < len(data):
		line = data[i]
		if line.startswith('hlf'):
			if line.endswith('a'):
				a /= 2
			else:
				b /= 2
		elif line.startswith('tpl'):
			if line.endswith('a'):
				a *= 3
			else:
				b *= 3
		elif line.startswith('inc'):
			if line.endswith('a'):
				a += 1
			else:
				b += 1
		elif line.startswith('jmp'):
			i += int(line[4:])
			continue
		elif line.startswith('jie'):
			if line.split(',')[0].endswith('a'):
				if a % 2 == 0:
					i += int(line.split(',')[1])
					continue
			else:
				if b % 2 == 0:
					i += int(line.split(',')[1])
					continue
		elif line.startswith('jio'):
			# Common Error People Made is that jio is "jump if ONE" and not odd
			if line.split(',')[0].endswith('a'):
				if a == 1:
					i += int(line.split(',')[1])
					continue
			else:
				if b == 1:
					i += int(line.split(',')[1])
					continue
		i += 1
	return b