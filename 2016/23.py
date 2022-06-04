import re

split_data = True
completed = True
raw_data = None # Not To be touched

# HEY! If you are reading this, I just want to tell you that there is an even more simpler way to solve this problem which people have discovered
# I won't be doing that method as it takes away the fun in solving this problem
# Here is where I found that solution at: https://www.reddit.com/r/adventofcode/comments/5jvbzt/comment/dbjbqtq/
# That method is super fast meaning, If I were to program it, it would be done in an instant
# However, I don't understand how they got that math so I will just stick to the method I will use


def solve(steps, register):
	index = 0

	def getValue(var):
		return register[var] if var in 'abcd' else int(var)

	# Compiling all the regexs
	cpy_re = re.compile(r'cpy (-?\d+|[abcd]) ([abcd])')
	inc_re = re.compile(r'inc ([abcd])')
	dec_re = re.compile(r'dec ([abcd])')
	jnz_re = re.compile(r'jnz ([abcd]|-?\d+) ([abcd]|-?\d+)')
	tgl_re = re.compile(r'tgl ([abcd]|-?\d+)')

	while index < len(steps):
		line = steps[index]

		if cpy_re.match(line):
			# Here is a simple promblem that part 2 hints at.
			# At one point we will stumble on instructions that look like this
			# ['cpy b c', 'inc a', 'dec c', 'jnz c -2', 'dec d', 'jnz d -5']
			# If you read this carefully, you will notice that a eventually becomes b multipled by d
			# Or in other words, first instruction, 1 character mulitpled by last instruction first character
			# If we directly do this, then it will speed up the program quite a lot
			# This part was inspired by https://github.com/kodsnack/advent_of_code_2016/blob/master/hbldh-python2and3/23.py

			if cpy_re.match(line) and inc_re.match(steps[index + 1]) and dec_re.match(steps[index + 2]) and jnz_re.match(steps[index + 3]) and dec_re.match(steps[index + 4]) and jnz_re.match(steps[index + 5]):
				# We have a stiuation where multiplication is being done
				registerToIncrement = inc_re.match(steps[index + 1]).groups()[0] # This is the register that we will increment
				supportRegister = dec_re.match(steps[index + 2]).groups()[0] # This is the register that will be used to multiply
				first_val = cpy_re.match(line).groups()[0] # This is the register from which the value will be multiplied. This won't reset to 0
				second_val = jnz_re.match(steps[index + 5]).groups()[0] # This is the register from which the value will be multiplied. This will reset to 0

				register[registerToIncrement] += getValue(first_val) * getValue(second_val)
				register[supportRegister] = 0
				register[second_val] = 0
				index += 6 # Skipping over the entire multiplication instruction
				continue
			else:
				value, letter = cpy_re.match(line).groups()
				register[letter] = getValue(value)
		elif inc_re.match(line):
			letter = inc_re.match(line).groups()[0]
			register[letter] += 1
		elif dec_re.match(line):
			letter = dec_re.match(line).groups()[0]
			register[letter] -= 1
		elif jnz_re.match(line):
			var, jump = jnz_re.match(line).groups()
			# Check if the var is not a 0
			if getValue(var) != 0:
				index += getValue(jump)
				continue
		elif tgl_re.match(line):
			var = tgl_re.match(line).groups()[0]
			lineIndex = index + getValue(var)
			if not (0 <= lineIndex < len(steps)):
				pass
			elif len(steps[lineIndex].split()) == 2:
				# We have one-argument instruction
				if steps[lineIndex].startswith('inc'):
					steps[lineIndex] = 'dec' + steps[lineIndex][3:]
				else:
					steps[lineIndex] = 'inc' + steps[lineIndex][3:]
			elif len(steps[lineIndex].split()) == 3:
				# We have two-argument instruction
				if steps[lineIndex].startswith('jnz'):
					steps[lineIndex] = 'cpy' + steps[lineIndex][3:]
				else:
					steps[lineIndex] = 'jnz' + steps[lineIndex][3:]
				 
		index += 1
	
	return register

def part1(data):
	register = {
		'a': 7,
		'b': 0,
		'c': 0,
		'd': 0
	}
	return solve(data, register)['a']

def part2(data):
	register = {
		'a': 12,
		'b': 0,
		'c': 0,
		'd': 0
	}
	return solve(data, register)['a']