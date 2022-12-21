#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import importlib
from os import path, makedirs
from time import time, gmtime
import argparse
from rich.console import Console
from rich.panel import Panel

console = Console()

try:
	import config
except ImportError:
	# Generate the config file
	print("You didn't have the config filem, so i created one! Please edit it and enter your session cookie in the file!")
	# Read the template
	with open('config-template.py','r') as file:
		lines = file.readlines()
	with open('config.py','w') as file:
		# Write the lines that do not start with a #
		[file.write(line) for line in lines if not line.startswith('#')]
	# Exit the program
	exit()

parser = argparse.ArgumentParser(description='Manually Enter Year and Day')
parser.add_argument('-d', '--day', type=int, help='The year of the day', default=config.day)
parser.add_argument('-y','--year', type=int, help='The day from which you require the answer', default=config.year)
args = parser.parse_args()

# Implementing some safety checks to ensure that the day and years are in the right range
if len(str(args.year)) == 2: # <- This will only work for the 20th century
	args.year = 2000 + args.year

tm_tuple = gmtime(time())

if not (0 < args.day<= 25):
	raise ValueError('The day is not in the right range!')
elif not (2015 <= args.year <= tm_tuple.tm_year):
	raise ValueError('The year is not in the right range!')
elif args.year == tm_tuple.tm_year and not args.day <= tm_tuple.tm_mday:
	raise ValueError('The day has not been revealed yet')


folder_path = f'{args.year}/'
txt_path = f'{args.year}/inputs/{args.day}.txt'
module_path = f'{args.year}/{args.day}'
raw_data = None

# collect the data
def collect_data(force) -> None:
	"""A simple function to calculate data"""
	global raw_data
	if not path.exists(txt_path) or force:
		# Make the input folder just incase
		try:
			makedirs(folder_path+'inputs')
		except FileExistsError:
			pass
		response = requests.get(f'https://adventofcode.com/{args.year}/day/{args.day}/input', cookies={'session':config.session_cookie})
		raw_data = response.text.strip('\n')
		# Save the data for backup
		if response.status_code == 200:
			with open(txt_path, 'w') as file:
				file.write(raw_data)
		elif response.status_code == 400 and raw_data == 'Puzzle inputs differ by user.  Please log in to get your puzzle input.':
			print(f"Hey looks like you need to provide a {'new ' if config.session_cookie else ''}session cookie!")
			exit()
		else:
			print(response.status_code, raw_data)
	else:
		with open(txt_path, 'r') as file:
			raw_data = ''.join(file.readlines())

# Create a setup
def setup() -> None:
	"""This function creates the folder with the template and the input sheet already in it"""
	global raw_data
	try:
		makedirs(folder_path+'inputs')
	except FileExistsError:
		pass
	collect_data(True)
	with open(module_path+'.py','w') as file:
		with open('runner_template.py','r') as template:
			lines = template.readlines()
			file.write(''.join(lines))

# Run the Code
def run_code() -> None:
	"""This function is responsible for running the code from the given year and day
	After the complete run of each part the answer is printed in the console with the amount of time it took to run"""
	module = importlib.import_module(module_path.replace('/','.'))
	if str(module.completed) != str(True):
		console.line()
		console.print('[bold]WARNING[/]: This answer is still not complete and it may be wrong', style='red')
		console.line()
		# print("\nWARNING: This answer is still not complete and it may be wrong\n")
	
	# Splitting the data into parts
	parseStart = time()
	if module.split_data == True:
		module.raw_data = raw_data.split('\n')
	elif isinstance(module.split_data, str):
		module.raw_data = [x.strip() for x in raw_data.split(module.split_data)]
	elif callable(module.split_data):
		module.raw_data = module.split_data(raw_data)
	else:
		module.raw_data = raw_data
	parseEnd = time()
	parseTime = (" + " + formatTime(parseEnd - parseStart)) if round(parseEnd - parseStart, 3) > 0 else ""

	# Part 1
	completion_map = {'True': chr(10004), '1': '~', 'False': 'X'} # 100 emoji and tick mark 
	console.rule(f'[spring_green4][{completion_map[str(module.completed)]}][/] Day {args.day} of {args.year}')
	with console.status('Running Part 1', spinner='aesthetic'):
		start = time()
		answer1 = module.part1(module.raw_data.copy() if isinstance(module.raw_data, (dict, list)) else raw_data)
		end = time()
	# If the total time is above 0.01 secounds then we show it in secounds otherwise we show it in milliseconds
	time_taken = formatTime(end - start)
	console.print(Panel(f"Answer to the 1st part: {answer1} ({time_taken}{parseTime})"))
	
	# Part 2
	with console.status('Running Part 2', spinner='aesthetic'):
		start = time()
		answer2 = module.part2(module.raw_data.copy() if isinstance(module.raw_data, (dict, list)) else raw_data)
		end = time()
	# print("The answer to the 2nd part is:", answer2)
	time_taken = formatTime(end - start)
	console.print(Panel(f"Answer to the 2nd part: {answer2} ({time_taken}{parseTime})"))
	# print(f"The 1st answer was calculated in just {time_taken}")

def formatTime(timeTaken:float) -> str:
	# timeTaken is in seconds
	if timeTaken > 60:
		return f'{timeTaken / 60:,.3}m'
	elif timeTaken >= .1:
		return f'{timeTaken:,.3}s'
	else:
		return f'{(timeTaken) * 1000:,.3}ms'

if __name__ == "__main__":
	if not path.exists(module_path+'.py'):
		print("Looks like this day has not been answered yet!")
		print("I will create a folder with the template for you to answer it ;)")
		setup()
		print("I have completed setting it up for you! Enjoy =)")
	else:
		print("Collecting Data",end="\r")
		collect_data(False)
		if not raw_data:
			print("Looks like the data doesn't exsist! Refetching data", end="\r")
			collect_data(True)
		print("Running Code...",end="\r")
		run_code()