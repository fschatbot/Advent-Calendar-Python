class InvalidOpCode(Exception):
	def __init__(self, instructions, ErrIndex):
		self.instructions = instructions
		self.ErrIndex = ErrIndex
	
	def __str__(self):
		return f'Invalid opcode at {self.ErrIndex}. Expected 1, 2, 99 got {self.instructions[self.ErrIndex]}'

def computer1(instructions:list, input1:int, input2:int) -> int:
	"""This computer is enough for day 2"""
	ins = instructions.copy()

	ins[1] = input1
	ins[2] = input2

	# Running the IntCode Computer
	i = 0
	while i < len(ins):
		if ins[i] == 1:
			ins[ins[i+3]] = ins[ins[i+1]] + ins[ins[i+2]]
			i += 4
		elif ins[i] == 2:
			ins[ins[i+3]] = ins[ins[i+1]] * ins[ins[i+2]]
			i += 4
		elif ins[i] == 99:
			break
		else:
			raise InvalidOpCode(ins, i)
	return ins[0]

def computer2(instructions:list, inp:int) -> int:
	"""This computer is enough for day 5, part 1"""
	ins = [int(x) for x in instructions.copy()]
	def getVal(index, mode): return ins[ins[index]] if mode == '0' else ins[index] # Returns the value based on the parameter mode

	outputs = []

	# Running the IntCode Computer
	i = 0
	while i < len(ins):
		# Over here we extract the op code and the parameter mode
		instruction = str(ins[i]).zfill(4)
		op_code = int(instruction[-2:])
		mode = instruction[:-2][::-1]
		# Over here we perform the op code instructions
		if op_code == 1:
			ins[ins[i+3]] = getVal(i+1, mode[0]) + getVal(i+2, mode[1])
			i += 4
		elif op_code == 2:
			ins[ins[i+3]] = getVal(i+1, mode[0]) * getVal(i+2, mode[1])
			i += 4
		elif op_code == 3:
			ins[ins[i+1]] = inp
			i += 2
		elif op_code == 4:
			outputs.append(getVal(i+1, mode[0]))
			i += 2
		elif op_code == 99:
			break
		else:
			raise InvalidOpCode(ins, i)
	return ins, ins[0], outputs

def computer3(instructions:list, inp:int) -> int:
	"""This computer is enough for day 5, part 2"""
	ins = [int(x) for x in instructions.copy()]
	def getVal(index, mode): return ins[ins[index]] if mode == '0' else ins[index] # Returns the value based on the parameter mode

	outputs = []

	# Running the IntCode Computer
	i = 0
	while i < len(ins):
		# Over here we extract the op code and the parameter mode
		instruction = str(ins[i]).zfill(4)
		op_code = int(instruction[-2:])
		mode = instruction[:-2][::-1]
		# Over here we perform the op code instructions
		if op_code == 1:
			ins[ins[i+3]] = getVal(i+1, mode[0]) + getVal(i+2, mode[1])
			i += 4
		elif op_code == 2:
			ins[ins[i+3]] = getVal(i+1, mode[0]) * getVal(i+2, mode[1])
			i += 4
		elif op_code == 3:
			ins[ins[i+1]] = inp
			i += 2
		elif op_code == 4:
			outputs.append(getVal(i+1, mode[0]))
			i += 2
		elif op_code == 5:
			if getVal(i+1, mode[0]) != 0:
				i = getVal(i+2, mode[1])
			else:
				i += 3
		elif op_code == 6:
			if getVal(i+1, mode[0]) == 0:
				i = getVal(i+2, mode[1])
			else:
				i += 3
		elif op_code == 7:
			if getVal(i+1, mode[0]) < getVal(i+2, mode[1]):
				ins[ins[i+3]] = 1
			else:
				ins[ins[i+3]] = 0
			i += 4
		elif op_code == 8:
			if getVal(i+1, mode[0]) == getVal(i+2, mode[1]):
				ins[ins[i+3]] = 1
			else:
				ins[ins[i+3]] = 0
			i += 4
		elif op_code == 99:
			break
		else:
			raise InvalidOpCode(ins, i)
	return ins, ins[0], outputs