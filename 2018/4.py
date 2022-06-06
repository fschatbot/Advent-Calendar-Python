#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import numpy as np

split_data = True
completed = True
raw_data = None # Not To be touched

def proccess_data(data:list) -> dict:
	# First we sort the entiries to form a chronological order
	date_re = re.compile(r'\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\]')
	def get_dates(entry:str) -> list:
		return [int(x) for x in date_re.findall(entry)[0]]

	data = sorted(data, key=get_dates)

	# Now we can start to process the data
	current_guard = None
	last_action = 0 # Which minute was the last action performed at
	date = None
	chart = {}

	# Entry Regex
	shift_re = re.compile(r'Guard #(\d+) begins shift')
	sleep_re = re.compile(r'falls asleep')
	wake_re = re.compile(r'wakes up')
	date_re = re.compile(r'\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\]')

	for entry in data:
		# First we update our chart with the current date
		year, month, day, _, minute = date_re.findall(entry)[0]
		date = f'{year}-{month}-{day}'

		if date not in chart:
			chart[date] = {'day': np.zeros(60, dtype=int), 'guard': None}
			last_action = 0

		# Now we can process the entry
		if shift_re.search(entry):
			current_guard = int(shift_re.search(entry).group(1))
		elif sleep_re.search(entry):
			last_action = int(minute)
		elif wake_re.search(entry):
			chart[date]['day'][last_action:int(minute)] = 1
		else:
			raise Exception(f'Unknown entry: {entry}')
		
		# Now we set the guard who is currrently working
		# This thing down below will only work if the shift command is the very first command per day
		if chart[date]['guard'] is None:
			chart[date]['guard'] = current_guard
	
	return chart

def part1(data) -> int:
	chart = proccess_data(data)

	# This is where we will find the guard who sleeps the most in general and the minute he sleeps the most
	# Now we can calculate the total minutes slept per guard
	guard_sleep = {}
	for date in chart:
		guard = chart[date]['guard']
		if guard not in guard_sleep:
			guard_sleep[guard] = 0
		guard_sleep[guard] += np.sum(chart[date]['day'])
	
	# Now we can find the guard that slept the most
	guard = max(guard_sleep, key=guard_sleep.get)

	# Now we compile all the sleeps for that guard
	guard_sleeps = []
	for date in chart:
		if chart[date]['guard'] == guard:
			guard_sleeps.append(chart[date]['day'])
	
	guard_sleeps = np.array(guard_sleeps)

	# Now we can find the minute that the guard slept the most
	minute = np.argmax(np.sum(guard_sleeps, axis=0))

	return guard * minute

def part2(data) -> int:
	chart = proccess_data(data)

	# This is where we find the guard who sleeps the most in a specific minute
	
	# First we seperate the chart based on the guard
	guard_chart = {}
	for date in chart:
		guard = chart[date]['guard']
		if guard not in guard_chart:
			guard_chart[guard] = []
		guard_chart[guard].append(chart[date]['day'])

	best = 0
	best_guard = None
	best_minute = None

	
	# We loop through each guard and find the one with the most sleep count

	for guard in guard_chart:
		# Get all his shifts info
		guard_sleeps = []
		for date in chart:
			if chart[date]['guard'] == guard:
				guard_sleeps.append(chart[date]['day'])

		guard_sleeps = np.array(guard_sleeps)

		# Find the minute he slept the most and how many times
		minute = np.argmax(np.sum(guard_sleeps, axis=0))
		count = np.sum(guard_sleeps[:, minute])
		# count = np.sum(guard_sleeps[:, minute]) / guard_sleeps.shape[0] <-- This is the best way to look as we would be dealing with probability

		if count > best:
			best = count
			best_guard = guard
			best_minute = minute

	return best_guard * best_minute
