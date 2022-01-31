split_data = False
completed = True
raw_data = None # Not To be touched

def follow_ins(ins):
	posx, posy = 0, 0
	poses = [(posx, posy)]
	for char in ins:
		if char == '^':
			posy += 1
		elif char == 'v':
			posy -= 1
		elif char == '>':
			posx += 1
		elif char == '<':
			posx -= 1
		poses.append((posx, posy))
	return poses

def part1(data):
	return len(set(follow_ins(data)))

def part2(data):
	# Turns out that all the even instructions are read by santa and all the odd instructions are read by robo-santa
	real_santa = data[::2]
	robo_santa = data[1::2]
	# We can get the santa positions follow instruction command
	poses_real = follow_ins(real_santa)
	poses_robo = follow_ins(robo_santa)
	# Next we put them in the same list, filter all the duplicates and return the length of the new list
	return len(set([*poses_real, *poses_robo]))