split_data = True
completed = True
raw_data = None # Not To be touched

def run_bootcode(instructions):
	accumulator = 0
	# Using while loop will give us a more dynamic control over the situation
	index = 0
	while index < len(instructions):
		# print(index, data[index])
		if instructions[index] == None:
			# We have run into a loop hence we break and return the value
			break
		elif instructions[index].startswith('nop'):
			# Make sure we set the instruction to null and increment the index
			instructions[index] = None
			index += 1
		elif instructions[index].startswith('acc'):
			accumulator += int(instructions[index][4:])
			# Make sure we set the instruction to null and increment the index
			instructions[index] = None
			index += 1
		elif instructions[index].startswith('jmp'):
			# Creating a copy of the index to be used later
			copy = instructions[index]
			# Make sure we set the instruction to null and increment the index
			instructions[index] = None
			index += int(copy[4:])
		else:
			raise Exception('Unknown instruction')
	# If we get here, we have reached the end of the list
	return index, accumulator

def part1(data):
	return run_bootcode(data)[1]

def part2(data):
	# This is one is just going to be trial and error
	index_neeeded = len(data)
	for i in data:
		if i.startswith('acc'):
			continue
		elif i.startswith('jmp'):
			# if the instruction is a jmp, we convert it to nop and see if the program works
			new_instructions = data.copy()
			new_instructions[data.index(i)] = 'nop' + i[3:]
			index, accumulator = run_bootcode(new_instructions)
			if index == index_neeeded:
				return accumulator
		elif i.startswith('nop'):
			# if the instruction is a nop, we convert it to jmp and see if the program works
			new_instructions = data.copy()
			new_instructions[data.index(i)] = 'jmp' + i[3:]
			index, accumulator = run_bootcode(new_instructions)
			if index == index_neeeded:
				return accumulator
		else:
			# IDK we will ever reach here
			raise Exception('Unknown instruction')