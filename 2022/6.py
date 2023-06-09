#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = False
completed = True
raw_data = None # Not To be touched

def part1(data):
	last3buffer = [buffer for buffer in data[:3]]
	for index, buffer in enumerate(data[3:], start=4):
		if len(set(last3buffer + [buffer])) == 4:
			return index
		last3buffer = last3buffer[1:] + [buffer]
	
	return "Something is wrong!"

def part2(data):
	last3buffer = [buffer for buffer in data[:13]]
	for index, buffer in enumerate(data[13:], start=14):
		if len(set(last3buffer + [buffer])) == 14:
			return index
		last3buffer = last3buffer[1:] + [buffer]
	
	return "Something is wrong!"