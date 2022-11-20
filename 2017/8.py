#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	register = {}
	
	def manager(name, value=None):
		if not value:
			return register.get(name, 0)
		else:
			register[name] = value
	
	for line in data:
		mod_reg, mod_op, mod_val, _, check_reg, check_op, check_val = line.split(' ')
		mod_val, check_val = int(mod_val), int(check_val)

		# Seeing if the check passes
		op_hashmap = { # <-- operation hashmap
			'==': lambda a, b: a == b,
			'!=': lambda a, b: a != b,
			'>=': lambda a, b: a >= b,
			'<=': lambda a, b: a <= b,
			'<': lambda a, b: a < b,
			'>': lambda a, b: a > b
		}
		# We get the respective function based on the operation and then evalute with the 2 values. If the answer is false skip this code
		if not op_hashmap[check_op](manager(check_reg), check_val): continue

		# Setting the values
		if mod_op == 'inc':
			manager(mod_reg, manager(mod_reg) + mod_val)
		else:
			manager(mod_reg, manager(mod_reg) - mod_val)
	
	# Returning the largest value in the register
	return max(register.values())


def part2(data):
	# Same code from part 1 but with few notable changes for extra speed and memory
	# 1. Instead of using the manager function, the commands are execute directly to cut down on if and else
	# 2. When setting the value, when we want to decrease we simply add it by its negative version
	register = {}
	maximum_value = 0
	
	for line in data:
		mod_reg, mod_op, mod_val, _, check_reg, check_op, check_val = line.split(' ')
		mod_val, check_val = int(mod_val), int(check_val)

		# Seeing if the check passes
		op_hashmap = { # <-- operation hashmap
			'==': lambda a, b: a == b,
			'!=': lambda a, b: a != b,
			'>=': lambda a, b: a >= b,
			'<=': lambda a, b: a <= b,
			'<': lambda a, b: a < b,
			'>': lambda a, b: a > b
		}
		# We get the respective function based on the operation and then evalute with the 2 values. If the evalutation is false, we skip this line
		if not op_hashmap[check_op](register.get(check_reg, 0), check_val): continue

		# Setting the values
		if mod_op == 'dec': mod_val *= -1 # Taking advantage of the fact that to subtract using addition we can use negative numbers
		register[mod_reg] = register.get(mod_reg, 0) + mod_val
		
		# maximum_value = max(*register.values(), maximum_value)
		# This is a much faster approch than the above one as we only compare it with changed register and not the entire registry
		maximum_value = max(register[mod_reg], maximum_value)
	
	# Returning the largest value in the register
	return maximum_value