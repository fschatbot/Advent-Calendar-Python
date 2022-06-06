#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	steps = {}

	def makeStep(name:str) -> None:
		if name not in steps:
			steps[name] = {
				"completed": False,
				"requirements": []
			}

	for line in data:
		line = line.split(' ')
		required, step = line[1], line[7]
		makeStep(step)
		makeStep(required)
		steps[step]["requirements"].append(required)
	
	def isAvalaible(step:str) -> bool:
		if steps[step]['completed']: return False
		elif steps[step] == []: return True
		else: return all(steps[minStep]["completed"] == True for minStep in steps[step]['requirements'])
	
	def get_all_steps() -> list:
		return [step for step in steps if isAvalaible(step)]
	
	steps_order = ""

	while len(steps_order) < len(steps.keys()):
		avaliable_steps = get_all_steps()
		avaliable_steps.sort()
		steps_order += avaliable_steps[0]
		steps[avaliable_steps[0]]["completed"] = True

	return steps_order

def part2(data):
	# This makes it easier to test things
	DELAY = 60
	WORKERS = 5

	# Proccessing the data and converting it into something that is understandable
	steps = {}
	workers = {i: None for i in range(WORKERS)}

	def makeStep(name:str) -> None:
		if name not in steps:
			steps[name] = {
				"completed": False,
				"CountDown": DELAY + ord(name) - ord('A'), # Even though an additional 1 should be added as per the question, 1 second is wasted as per the current code to figure out that the countdown is 0 
				"worker": None,
				"requirements": []
			}

	for line in data:
		line = line.split(' ')
		required, step = line[1], line[7]
		makeStep(step)
		makeStep(required)
		steps[step]["requirements"].append(required)
	
	def isAvalaible(step:str) -> bool:
		if steps[step]['completed'] or steps[step]['worker'] != None: return False
		elif steps[step] == []: return True
		else: return all(steps[minStep]["completed"] == True for minStep in steps[step]['requirements'])
	
	def get_all_steps() -> list:
		return [step for step in steps if isAvalaible(step)]
	
	# This is where all the magic happens
	steps_order = ""
	seconds = 0

	while len(steps_order) < len(steps.keys()):
		seconds += 1
		# Handle the contruction of steps that the workers are performing
		for worker, step in workers.items():
			# Skip the workers that are not working
			if not step:
				continue
			# If the step is completed, mark it as done and remove it from the worker
			elif steps[step]['CountDown'] == 0:
				steps[step]['completed'] = True
				workers[worker] = None
				steps_order += step
			else:
				# Decrement the countdown
				steps[step]["CountDown"] -= 1
		
		# Check if we have any avaliable steps and assign them to the workers who are free
		avaliable_steps = get_all_steps()
		avaliable_steps.sort()
		for step in avaliable_steps:
			for worker, curr_job in workers.items():
				if curr_job == None:
					workers[worker] = step
					steps[step]['worker'] = worker
					break
		
		# Pretty Printing the current state of the workers
		# print(f"{str(seconds-1).rjust(4, '0')} - {' '.join(job or '.' for worker, job in workers.items())} - {steps_order.ljust(len(steps.keys()), '.')}")
		
	
	return seconds - 1
