#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(data):
	lines = data.split('\n')
	register = {
		'A': int(lines[0].split(': ')[1]),
		'B': int(lines[1].split(': ')[1]),
		'C': int(lines[2].split(': ')[1]),
	}
	instructions = lines[4].split(': ')[1].split(',')
	return register, [int(x) for x in instructions]

split_data = parse
completed = True
raw_data = None # Not To be touched

def part1(data):
	register, instructions = data

	def combo(oprand):
		if 0 <= oprand <= 3:
			return oprand
		elif oprand == 4:
			return register['A']
		elif oprand == 5:
			return register['B']
		elif oprand == 6:
			return register['C']
		else:
			raise "How are we executing a reserved value?"

	pointer = 0
	output = []
	while pointer < len(instructions):
		opcode = instructions[pointer]
		oprand = instructions[pointer+1]

		match opcode:
			case 0:
				register['A'] = int(register['A'] / (2**combo(oprand)))
				pointer += 2
			case 1:
				register['B'] = register['B'] ^ oprand
				pointer += 2
			case 2:
				register['B'] = combo(oprand) % 8
				pointer += 2
			case 3:
				if register['A'] == 0:
					pointer += 2
				else:
					pointer = oprand
			case 4:
				register['B'] = register['B'] ^ register['C']
				pointer += 2
			case 5:
				output.append(str(combo(oprand) % 8))
				pointer += 2
			case 6:
				register['B'] = int(register['A'] / (2**combo(oprand)))
				pointer += 2
			case 7:
				register['C'] = int(register['A'] / (2**combo(oprand)))
				pointer += 2
			case default:
				raise "ERR"

	# print(pointer, output, register)
	return ','.join(output)


def compute(register, instructions):
	pointer = 0
	output = []
	while pointer < len(instructions):
		opcode = instructions[pointer]
		oprand = instructions[pointer+1]
		combo = ({4:register['A'],5:register['B'],6:register['C']}).get(oprand, oprand)

		match opcode:
			case 0:
				register['A'] = int(register['A'] / (2**combo))
				pointer += 2
			case 1:
				register['B'] = register['B'] ^ oprand
				pointer += 2
			case 2:
				register['B'] = combo % 8
				pointer += 2
			case 3:
				if register['A'] == 0:
					pointer += 2
				else:
					pointer = oprand
			case 4:
				register['B'] = register['B'] ^ register['C']
				pointer += 2
			case 5:
				output.append(combo % 8)
				if len(output) > len(instructions) or output[-1] != instructions[len(output)-1]: return False
				pointer += 2
			case 6:
				register['B'] = int(register['A'] / (2**combo))
				pointer += 2
			case 7:
				register['C'] = int(register['A'] / (2**combo))
				pointer += 2
	
	return output == instructions

def part2(data):
	"""
	Forget about getting the answer by brute forcing it. 
	It's not going to happen as the values we are looking for are too large
	A much simpler method is backtracking. We can look at our program and notice a few things

	My program:

		B = A mod 8
		B = B XOR 7
		C = A / 2**B
		A = A / 8
		B = B XOR 7
		B = B XOR C
		OUT (B mod 8)
		if A != 0 then jump 0


	It ends with 3,0 aka if A != 0 then jump 0
	and the only modification done to A is A = A / 2**3

	Thus we know that our A should end in 0 for the program to halt which leaves us with a range of for A at the start [0*8, 1*8)
	The range equals out to 0,1,2,3,4,5,6,7. `[]` brackets means inclusive and `()` brackets mean exclusive.

	Running these possibilities through the program we can see that only 0 and 7 output a `0`.
	As A can't with a 0 (as it would cause the program to halt in the previous cycle) we know the program will have to have a 7 at the start.
	Thus in the last cycle we begin with a 7 to allow the program to halt and also give us the required `0` as output
	Now we can extend the same logic backwards. Now we check the [7*8, (7+1)*8) interval for a 3 as output giving us 58 and 60.
	Thus creating the interval [58*8,(58+1)*8) and [60*8, (60+1)*8) to check for the third last value and so on...

	Summary:
	last value: [0*8, 1*8) interval that outputs 0
	2nd last value: [7*8, (7+1)*8) interval that outputs 3
	3rd last value: [58*8,(58+1)*8) and [60*8, (60+1)*8) interval that outputs x
	and so on...

	As we are checking at max 8n possibilities for a single cycle where n averages at ~8 we should not have to look for much

	Thus we get values of A which all end up producing the output we want. This may only work my input
	"""

	_, program = data

	
	def output(A):
		return ((A % 8)^7^7 ^ int(A / 2**((A % 8) ^ 7))) % 8 # Simplified version 
		print(A)
		B = A % 8
		B = A ^ 7
		C = int(A / 2**B)
		A = int(A / 8)
		B = B ^ 7
		B = B ^ C
		return B % 8

	growth = [0]
	n = []
	for out in program[::-1]:
		growth = [x for a in growth for x in range(a*8, (a+1)*8) if x != 0 and output(x) == out]
		n.append(len(growth))
	return growth[0]

"""
Program: 2,4 1,7 7,5 0,3 1,7 4,1 5,5 3,0

B = A mod 8
B = B XOR 7 (7,6,5,4,3,2,1,0 as possibilities)
C = A / 2**B
A = A / 8
B = B XOR 7 (0,1,2,3,4,5,6,7 as possibilities)
B = B XOR C
OUT B mod 8
if A != 0 then jump 0

```
def check(A):
  return ((A % 8) ^ int(A / 2**((A % 8) ^ 7))) % 8

growth = [0]
n = []
for output in (2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0)[::-1]:
	growth = [x for a in growth for x in range(a*8, (a+1)*8) if x != 0 and check(x) == output]
	n.append(len(growth))

growth[0]
```



The output is being done by B essentially. 
We can manually back track the entire fucking thing...

The only way to terminate the program is if A started less than 8
We get 0 as output if A was 0 or 7 at the start.

Knowing the logic of the program. We check [0*8, 1*8) and [7*8, 8*8) for output of 3.
Sure enough the outputs 3, 58, and 60 all produce 3 which go on to produce 0.
Thus we check for [3*8,4*8), [58*8, 59*8), and [60*8, 61*8) for production of 5.
and so on and we are bound to find the value...

Note: 0 can't be a possibility since it would mean that mean it would have terminated before...





Thus the next values we look

Hence A started out with <8
B = 7 - A
C = A / 2**(7-A) (0,1,3,7 as possible values)
B = A


"""