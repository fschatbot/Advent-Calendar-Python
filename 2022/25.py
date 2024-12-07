#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	charMap = {'=':-2, '-':-1, '0':0, '1':1, '2':2}
	def SNAFUtoDECIMAL(snafu):
		return sum(5**(len(snafu)-p)*charMap[num] for p, num in enumerate(snafu, start=1))

	total = sum(SNAFUtoDECIMAL(line) for line in data)
	print("Total Fuel:", total)
	
	# Now comes the hard part
	SNAFU = []

	while total > SNAFUtoDECIMAL(SNAFU):
		SNAFU.append('2')
	
	l = ['2', '1', '0', '-', '=']
	
	for index in range(len(SNAFU)):
		for a in l:
			if SNAFUtoDECIMAL(SNAFU[:index]+[a]+SNAFU[index+1:]) - total < 0: break
			SNAFU[index] = a
	
	return ''.join(SNAFU)

def part2(data):
	...