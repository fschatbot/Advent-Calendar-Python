from typing import List, Tuple, Literal

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

def computer3(instructions:list, inputs:List[int]) -> List[int]:
	"""This computer is enough for day 5 part 2 and day 7 part 1"""
	ins = [int(x) for x in instructions.copy()]
	def getVal(index, mode): return ins[ins[index]] if mode == '0' else ins[index] # Returns the value based on the parameter mode

	outputs = []
	inps = inputs.copy()

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
			ins[ins[i+1]] = inps.pop(0)
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
	return outputs

class computer4:
	"""This computer gives more control over the code"""
	def __init__(self, instructions:List[int]) -> None:
		self.ins = instructions
		self.inps = []
		self.outs = []
		self.halted = False
		self.pointer = 0
	
	# These functions allow for control
	def input(self, *inp:int) -> None:
		self.inps.extend(inp)
	
	# These functions allow the computer to run
	def getVal(self, index:int, mode:Literal['0', '1']) -> int:
		"""Return value from index based on the mode provided. 0 stands for positional mode and 1 stands fo literal mode."""
		return self[self[index]] if mode == '0' else self[index]
	
	def __getitem__(self, __index):
		"""Get instruction from index"""
		return self.ins[__index]
	def __setitem__(self, __index, __value):
		"""Set instruction from index"""
		self.ins[__index] = __value

	@classmethod
	def from_instructions(cls, instructions:list) -> """computer4""":
		return cls([int(x) for x in instructions.copy()])

	# Runner Functions
	def run_once(self):
		"""Runs the IntCode once. TODO: Fix this function"""
		if self.halted: raise RuntimeError("The computer has already halted")
		if self.pointer >= len(self.ins): raise RuntimeError("The index pointer is out of range")
		
		# Over here we extract the op code and the parameter mode
		i = self.pointer
		instruction = str(self[i]).zfill(4)
		op_code = int(instruction[-2:])
		mode = instruction[:-2][::-1]
		# Over here we perform the op code instructions
		if op_code == 1:
			self[self[i+3]] = self.getVal(i+1, mode[0]) + self.getVal(i+2, mode[1])
			i += 4
		elif op_code == 2:
			self[self[i+3]] = self.getVal(i+1, mode[0]) * self.getVal(i+2, mode[1])
			i += 4
		elif op_code == 3:
			self[self[i+1]] = self.inps.pop(0)
			i += 2
		elif op_code == 4:
			self.outs.append(self.getVal(i+1, mode[0]))
			i += 2
		elif op_code == 5:
			if self.getVal(i+1, mode[0]) != 0:
				i = self.getVal(i+2, mode[1])
			else:
				i += 3
		elif op_code == 6:
			if self.getVal(i+1, mode[0]) == 0:
				i = self.getVal(i+2, mode[1])
			else:
				i += 3
		elif op_code == 7:
			if self.getVal(i+1, mode[0]) < self.getVal(i+2, mode[1]):
				self[self[i+3]] = 1
			else:
				self[self[i+3]] = 0
			i += 4
		elif op_code == 8:
			if self.getVal(i+1, mode[0]) == self.getVal(i+2, mode[1]):
				self[self[i+3]] = 1
			else:
				self[self[i+3]] = 0
			i += 4
		elif op_code == 99:
			self.halted = True
		else:
			raise ValueError(f"Invalid op code recived. Expected 1-8 and 99 got {op_code}")
		self.pointer = i
	
	def run_till_output(self) -> int:
		"""Keeps running the code till their is an output"""
		old_out_len = len(self.outs)
		while not self.halted and old_out_len == len(self.outs):
			self.run_once()
		return self.recent_output
	
	def run_till_end(self):
		"""Keeps running the code till it halts"""
		while not self.halted:
			self.run_once()
	
	# Properties
	@property
	def recent_output(self) -> int:
		return self.outs[-1]