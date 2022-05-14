split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	register = {
		'a': 0,
		'b': 0,
		'c': 0,
		'd': 0
	}
	index = 0
	while index < len(data):
		line = data[index]
		if line.startswith('cpy'):
			value, letter = line.split()[1:]
			if value in register:
				register[letter] = register[value]
			else:
				register[letter] = int(value)
		elif line.startswith('inc'):
			letter = line.split()[1]
			register[letter] += 1
		elif line.startswith('dec'):
			letter = line.split()[1]
			register[letter] -= 1
		elif line.startswith('jnz'):
			var, jump = line.split()[1:]
			if var.isdigit() and int(var) != 0:
				index += int(jump)
				continue
			elif register[var] != 0:
				index += int(jump)
				continue
		index += 1
	return register['a']


def part2(data):
	# Same code as part 1, but with a different register
	register = {
		'a': 0,
		'b': 0,
		'c': 1,
		'd': 0
	}
	index = 0
	while index < len(data):
		line = data[index]
		if line.startswith('cpy'):
			value, letter = line.split()[1:]
			if value in register:
				register[letter] = register[value]
			else:
				register[letter] = int(value)
		elif line.startswith('inc'):
			letter = line.split()[1]
			register[letter] += 1
		elif line.startswith('dec'):
			letter = line.split()[1]
			register[letter] -= 1
		elif line.startswith('jnz'):
			var, jump = line.split()[1:]
			if var.isdigit() and int(var) != 0:
				index += int(jump)
				continue
			elif register[var] != 0:
				index += int(jump)
				continue
		index += 1
	return register['a']