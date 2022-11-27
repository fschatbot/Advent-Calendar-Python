class InvalidOpCode(Exception):
	def __init__(self, instructions, ErrIndex):
		self.instructions = instructions
		self.ErrIndex = ErrIndex
	
	def __str__(self):
		return f'Invalid opcode at {self.ErrIndex}. Expected 1, 2, 99 got {self.instructions[self.ErrIndex]}'

def computer(instructions:list, input1:int, input2:int) -> int:
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