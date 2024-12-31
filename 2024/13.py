#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import findall

def parse(data):
	machines = []

	for machine in data.split("\n\n"):
		Ax,Ay,Bx,By,Px,Py = findall(r"(\d+)", machine)
		machines.append((int(Ax),int(Ay),int(Bx),int(By),int(Px),int(Py)))

	return machines

split_data = parse
completed = True
raw_data = None # Not To be touched

def part1(data):
	# This can be solved quickly using some simple math
	tokens = 0
	for machine in data:
		Ax,Ay,Bx,By,Px,Py = machine

		for Bpress in range(101):
			pending = Px - Bpress*Bx
			if pending < 0: break # Looks like we are over shooting here...
			Apress = pending / Ax
			if Apress % 1 != 0 or Apress > 100:
				continue # Not a valid solution

			# By now Bpress is atmost 100, Apress is atmost 100 and both are integers
			if Bpress*By + Apress*Ay == Py:
				assert Apress*Ax + Bpress*Bx == Px # Just a flex!
				tokens += Apress*3 + Bpress
				break
	
	return int(tokens)

def part2(data):
	# We can do some simple math on paper and come up with the formula
	# Ax * x + Bx * y = Px
	# Ay * x + By * y = Py

	# https://www.desmos.com/calculator/h566btcmir 

	tokens = 0
	for machine in data:
		Ax,Ay,Bx,By,Px,Py = machine
		Px += 10000000000000 # The only change
		Py += 10000000000000 # The only change

		aPress = ((By*Px) - (Bx*Py))/((By*Ax) - (Bx*Ay))
		if aPress % 1 != 0 or aPress < 0: continue # We only accept integer solutions
		bPress = (Px - aPress*Ax)/Bx
		if bPress % 1 != 0 or aPress < 0: continue # We only accept integer solutions

		# print(aPress, bPress)
		assert aPress*Ax + bPress*Bx == Px and aPress*Ay + bPress*By == Py # Just a flex!
		tokens += aPress*3 + bPress

	
	return int(tokens)