#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def parse(data):
	return map(int, re.findall(r'\d+', data))

split_data = parse
completed = True
raw_data = None # Not To be touched

def generator(start, factor):
	val = start
	while True:
		val = val * factor % 2147483647
		yield val

def part1(data):
	generatorA_start, generatorB_start = data
	counter = 0
	generatorA = generator(generatorA_start, 16807)
	generatorB = generator(generatorB_start, 48271)
	for _ in range(40_000_000):
		valueA = generatorA.__next__()
		valueB = generatorB.__next__()
		if valueA & 0xFFFF == valueB & 0xFFFF: counter += 1
	return counter

def part2(data):
	generatorA_start, generatorB_start = data
	counter = 0
	generatorA = generator(generatorA_start, 16807)
	generatorB = generator(generatorB_start, 48271)
	for _ in range(5_000_000):
		# Generator A picking a value divisible by 4
		valueA = generatorA.__next__()
		while valueA % 4 != 0: valueA = generatorA.__next__()
		# Generator B picking a value divisible by 8
		valueB = generatorB.__next__()
		while valueB % 8 != 0: valueB = generatorB.__next__()
		# Comparing both the values
		if valueA & 0xFFFF == valueB & 0xFFFF: counter += 1
	return counter