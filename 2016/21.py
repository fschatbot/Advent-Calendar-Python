import re
from itertools import permutations

split_data = True
completed = True
raw_data = None # Not To be touched

def scramble(password, scramble_steps):
	password = [i for i in password]

	# Compiling all the regexes
	SwapPos = re.compile(r"swap position (\d+) with position (\d+)")
	SwapLet = re.compile(r"swap letter (\w) with letter (\w)")
	Rotate = re.compile(r"rotate (left|right) (\d+) step")
	RotatePos = re.compile(r"rotate based on position of letter (\w)")
	Reverse = re.compile(r"reverse positions (\d+) through (\d+)")
	Move = re.compile(r"move position (\d+) to position (\d+)")

	# Now we scramble the password
	for line in scramble_steps:
		if SwapPos.match(line):
			i1, i2 = SwapPos.match(line).groups()
			i1, i2 = int(i1), int(i2)
			password[i1], password[i2] = password[i2], password[i1]
		elif SwapLet.match(line):
			l1, l2 = SwapLet.match(line).groups()
			i1, i2 = password.index(l1), password.index(l2)
			password[i1], password[i2] = password[i2], password[i1]
		elif Rotate.match(line):
			direction, steps = Rotate.match(line).groups()
			steps = int(steps)
			if direction == "right":
				password = password[-steps:] + password[:-steps]
			else:
				password = password[steps:] + password[:steps]
		elif RotatePos.match(line):
			letter = RotatePos.match(line).groups()[0]
			i = password.index(letter) + 1
			if password.index(letter) >= 4:
				i += 1			
			# Thanks: https://www.geeksforgeeks.org/python-ways-to-rotate-a-list/
			password = [password[(j - i) % len(password)] for j, _ in enumerate(password)]
		elif Reverse.match(line):
			i1, i2 = Reverse.match(line).groups()
			i1, i2 = int(i1), int(i2)
			password = password[:i1] + password[i1:i2+1][::-1] + password[i2+1:]
		elif Move.match(line):
			i1, i2 = Move.match(line).groups()
			i1, i2 = int(i1), int(i2)
			l1 = password[i1]
			password.remove(l1)
			password.insert(i2, l1)

	return ''.join(password)

def part1(data):
	return scramble("abcdefgh", data)

def part2(data):
	# Here is a simple trick that can help us save time
	# We would simply try all the variations of the password and put it the scrambler
	# If the scrambled password from the scrambler is the same as the original scramble
	# then we know what the password is
	
	scrambled = "fbgdceah"
	possible = []
	for i in permutations(scrambled):
		if scramble(i, data) == scrambled:
			possible.append(''.join(i))
	# There can be multiple possibilities, so we return the first one
	return possible[0]
