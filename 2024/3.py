#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

split_data = False
completed = True
raw_data = None # Not To be touched


def part1(data):
	mul = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)
	cum = 0
	for num1, num2 in mul:
		cum += int(num1) * int(num2)
	
	return cum

def part2(data):
	compiled = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")

	ignore = False
	cum = 0
	for out in compiled.finditer(data):
		if out.group() == 'do()':
			ignore = False
		elif out.group() == "don't()":
			ignore = True
		elif not ignore:
			cum += int(out.group(1)) * int(out.group(2))

	return cum