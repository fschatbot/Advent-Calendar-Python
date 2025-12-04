#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
from itertools import product

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data:List[str]):
	result = 0

	for line in data:
		output, numbers = line.split(': ')
		numbers = numbers.split(' ')

		for operators in product(['+', '*'], repeat=len(numbers) - 1):
			equation = int(numbers[0])
			for op, num in zip(operators, numbers[1:]):
				if op == '+':
					equation += int(num)
				else:
					equation *= int(num)
			
			if equation == int(output):
				result += int(output)
				break
	
	return result

def part2(data:List[str]):
	result = 0

	for line in data:
		output, numbers = line.split(': ')
		numbers = numbers.split(' ')

		for operators in product(['+', '*', '||'], repeat=len(numbers) - 1):
			equation = int(numbers[0])
			for op, num in zip(operators, numbers[1:]):
				if op == '+':
					equation += int(num)
				elif op == '*':
					equation *= int(num)
				else:
					equation = int(str(equation)+num)
			
			if equation == int(output):
				result += int(output)
				break
	
	return result