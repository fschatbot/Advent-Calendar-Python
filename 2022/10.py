#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	registerX = 1
	signalStrenghtAcc = 0

	cycle = 0
	ins = 0
	wait = False
	while cycle <= 220 and ins < len(data): # Only need these many cycles
		cycle += 1
		if cycle % 40 == 20:
			signalStrenghtAcc += registerX * cycle
		
		# The cycle is over
		
		if wait == True and data[ins].startswith('addx'):
			registerX += int(data[ins].split(' ')[1])
			wait = False
			ins += 1
		elif wait == False  and data[ins].startswith('addx'):
			wait = True # Wait out till the next cycle
		elif data[ins].startswith('noop'):
			ins += 1
	return signalStrenghtAcc

def part2(data):
	spriteMid = 1

	screen = []

	cycle = 0
	ins = 0
	wait = False
	while ins < len(data): # Only need these many cycles
		if cycle % 40 == 0: screen.append('')
		cycle += 1

		# During the cycle
		# print(f"During cycle  {cycle}: CRT draws pixel in position {cycle % 40 - 1}")
		if abs(spriteMid - ((cycle-1) % 40)) <= 1:
			screen[-1] += '\u2588' # \u2588 - Full block, makes it easier to read
		else:
			screen[-1] += ' '
		# print(f"Current CRT row: {screen[-1]}")
		
		# The cycle is over
		if wait == True and data[ins].startswith('addx'):
			spriteMid += int(data[ins].split(' ')[1])
			# print(f"End of cycle  {cycle}: finish executing {data[ins]} (Register X is now {spriteMid})")
			wait = False
			ins += 1
		elif wait == False  and data[ins].startswith('addx'):
			# print(f"End of cycle  {cycle}: begin executing {data[ins]}")
			wait = True # Wait out till the next cycle
		elif data[ins].startswith('noop'):
			ins += 1
	
	for row in screen: print(''.join(row))
	print('This time, there will be no returned output as its super hard to guess all the letter patterns. However, a human can read the above display and figure out the output!')