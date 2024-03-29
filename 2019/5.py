#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .intcode import computer2, computer3

split_data = ','
completed = True
raw_data = None # Not To be touched

def part1(data):	
	_, _, outputs = computer2(data, 1)
	return outputs[-1]

def part2(data):
	outputs = computer3(data, [5])
	return outputs[-1]