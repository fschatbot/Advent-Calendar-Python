#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import os

def parse(data:str):
	robots = []
	for line in data.split("\n"):
		p, v = line.split(' ')
		p = p[2:].split(',')
		v = v[2:].split(',')
		robots.append(((int(p[0]), int(p[1])), (int(v[0]), int(v[1]))))
	
	return robots

split_data = parse
completed = True
raw_data = None # Not To be touched

def part1(data):
	bx, by = 101, 103
	quadrants = [0, 0, 0, 0]

	# Simulation
	for robot in data:
		# Instant 100s simulation
		((x, y), (vx, vy)) = robot
		nx = (x + vx * 100) % bx
		ny = (y + vy * 100) % by

		# Figuring out which quadrant the robot is in.
		if nx < bx // 2:
			if ny < by // 2:
				quadrants[0] += 1
			elif ny > by // 2:
				quadrants[1] += 1
		elif nx > bx // 2:
			if ny < by // 2:
				quadrants[2] += 1
			elif ny > by // 2:
				quadrants[3] += 1
	
	# print(quadrants)
	return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def part2(data):
	bx, by = 101, 103

	os.makedirs("2024/14", exist_ok=True)

	# Simulation
	robots = data
	for i in range(1, 10_001):
		nRobots = []

		# Gray scale image
		img = Image.new('L', (bx, by), 255)
		for robot in robots:
			# Instant 100s simulation
			((x, y), (vx, vy)) = robot
			nx = (x + vx) % bx
			ny = (y + vy) % by

			# Drawing the robot
			img.putpixel((nx, ny), 0)

			nRobots.append(((nx, ny), (vx, vy)))
		
		# Save the image
		img.save(f"2024/14/{i}.png")
		robots = nRobots
	


	print("Please open the folder 2024/14 and search for the file that forms a christmas tree. You will see 10,000 images and one of them forms the christmas tree.")