split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	# Before you start reading the code, I just want to say, this is the worst way to torture your employees
	# Like, why the heck would you lock the bathroom and why would tell the employees to memorize this code?
	# Good thing this program exsist, otherwise they would have to pee in the pants
	coords = [1, 1]
	keypad = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]

	code = ""

	for line in data:
		for c in line:
			if c == 'U':
				coords[1] = max(coords[1] - 1, 0)
			elif c == 'D':
				coords[1] = min(coords[1] + 1, 2)
			elif c == 'L':
				coords[0] = max(coords[0] - 1, 0)
			elif c == 'R':
				coords[0] = min(coords[0] + 1, 2)
		code += str(keypad[coords[1]][coords[0]])
	return code

def part2(data):
	coords = [2, 0]
	keypad = [
		[None, None, '1', None, None],
		[None, '2', '3', '4', None],
		['5', '6', '7', '8', '9'],
		[None, 'A', 'B', 'C', None],
		[None, None, 'D', None, None]
	]
	
	code = ""

	for line in data:
		for c in line:
			if c == 'U':
				temp = max(coords[0] - 1, 0)
				# Check if the new coords are valid
				if keypad[temp][coords[1]] != None:
					coords[0] = temp
			elif c == 'D':
				temp = min(coords[0] + 1, 4)
				if keypad[temp][coords[1]] != None:
					coords[0] = temp
			elif c == 'L':
				temp = max(coords[1] - 1, 0)
				if keypad[coords[0]][temp] != None:
					coords[1] = temp
			elif c == 'R':
				temp = min(coords[1] + 1, 4)
				if keypad[coords[0]][temp] != None:
					coords[1] = temp
		code += keypad[coords[0]][coords[1]]
	return code