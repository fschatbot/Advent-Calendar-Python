#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

split_data = '-'
completed = True
raw_data = None # Not To be touched

def part1(data):
	min, max = int(data[0]), int(data[1])
	regex = re.compile(r'(.)\1') # <-- Slight decrease in time

	valid = 0
	for password in range(min, max):
		passStr = str(password)

		if len(passStr) != 6: continue # <-- Looking for 6 characters
		if not regex.findall(passStr): continue # <-- Looking for repetition
		if not all(int(passStr[i]) >= int(passStr[i-1]) for i in range(1, len(passStr))): continue # <-- Making sure that a number is at least the previous number
		# print(passStr)
		valid += 1
	
	return valid

def part2(data):
	min, max = int(data[0]), int(data[1])
	regex = re.compile(r'(.)\1') # <-- Slight decrease in time

	valid = 0
	for password in range(min, max):
		passStr = str(password)

		if len(passStr) != 6: continue # <-- Looking for 6 characters
		if not regex.findall(passStr): continue # <-- Looking for repetition
		if match := regex.findall(passStr):
			# Making sure that the matchs are not part of a bigger group
			if all(x*3 in passStr for x in match): continue
			# Now check if all the repetitions are being repeated 3 times
		if not all(int(passStr[i]) >= int(passStr[i-1]) for i in range(1, len(passStr))): continue # <-- Making sure that a number is at least the previous number
		# print(passStr)
		valid += 1
	
	return valid