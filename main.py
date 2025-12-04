#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import importlib
import regex as re
from os import path, makedirs
from time import time, gmtime, sleep
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
parser.add_argument('-sub', '--submit', action='store_true', help='Submit the answer to the server')
args = parser.parse_args()

# Implementing some safety checks to ensure that the day and years are in the right range
if len(str(args.year)) == 2: # <- This will only work for the 20th century
	args.year = 2000 + args.year

tm_tuple = gmtime(time())

if not (0 < args.day<= 25):
	raise ValueError('The day is not in the right range!')
elif not (2015 <= args.year <= tm_tuple.tm_year):
	raise ValueError('The year is not in the right range!')
elif args.year == tm_tuple.tm_year and args.day > tm_tuple.tm_mday:
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
		try:
			response = requests.get(f'https://adventofcode.com/{args.year}/day/{args.day}/input', cookies={'session':config.session_cookie}, headers={'User-Agent': 'github.com/fschatbot/Advent-Calendar-Python/ by FSChatbot'})
		except requests.exceptions.ConnectionError:
			console.print("[red bold]Seems like we are having some issues with the internet!!")
			exit()
		raw_data = response.text.strip('\n')
		# Save the data for backup
		if response.status_code == 200:
			with open(txt_path, 'w') as file:
				file.write(raw_data)
		elif response.status_code == 400 and raw_data == 'Puzzle inputs differ by user.  Please log in to get your puzzle input.':
			console.print(f"[red]Hey looks like you need to provide a {'new ' if config.session_cookie else ''}session cookie!")
			exit()
		elif response.status_code == 404 and "Please don't repeatedly request this endpoint before it unlocks!" in raw_data:
			console.print(f"[red]Looks like the question for this day has not been revealed yet!")
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


def submit_code(answer, level) -> None:
	if not args.submit: return
	if answer is None: return

	res = requests.post(f'https://adventofcode.com/{args.year}/day/{args.day}/answer', headers={
		'cookie': f'session={config.session_cookie}',
		'content-type': 'application/x-www-form-urlencoded'
	}, data={
		'level': level,
		'answer': answer
	})

	out = res.text.strip()
	open('debug.html','w', encoding='utf-8').write(out)

	response = re.findall(f'<article>(.*?)</article>', out.replace('\n',''))
	response = re.sub(r'<[^>]*?>', '', response[0])

	if 'That\'s the right answer!' in out:
		console.print(f"Answer was [bold green]correct[/]! (Sleeping for 5s...)")
		sleep(5) # Sleep for 10 seconds to avoid getting rate limited
	elif "You don't seem to be solving the right level" in out:
		console.print(f"[cyan]Looks like we already solved this one =)")
	elif "You gave an answer too recently;" in out:
		seconds = re.search(r'You have (\d+)s left to wait.', response).group(1)
		console.print(f"[bold red]Rate Limited[/]! Sleeping for {seconds}s...")
		sleep(int(seconds)+1)
		submit_code(answer, level)
	else:
		console.print(f'Answer was [bold red]incorrect[/]!\nServer Response: {response}')
		sleep(10) # Sleep for 10 seconds to avoid getting rate limited		

	

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
	
	if args.submit:
		console.print("[bold cyan]INFO[/]: Whatever the output is, it will be submitted to the server")
	
	def data_parser(data):
		if module.split_data == True:
			return data.split('\n')
		elif isinstance(module.split_data, str):
			return [x.strip() for x in data.split(module.split_data)]
		elif callable(module.split_data):
			return module.split_data(data)
		else:
			return data

	# Data Parsing for part 1
	parseStart = time()
	module.raw_data = data_parser(raw_data)
	parseEnd = time()
	parseTime = (" + " + formatTime(parseEnd - parseStart)) if round(parseEnd - parseStart, 3) > 0 else ""

	# Running Part 1
	completion_map = {'True': '\u2714', '1': '~', 'False': '\u2718'}
	console.rule(f'[spring_green4][{completion_map[str(module.completed)]}][/] Day {args.day} of {args.year}')
	with console.status('Running Part 1', spinner='aesthetic'):
		start = time()
		answer1 = module.part1(module.raw_data)
		end = time()
	# If the total time is above 0.01 secounds then we show it in secounds otherwise we show it in milliseconds
	time_taken = formatTime(end - start)
	console.print(Panel(f"Answer to the 1st part: {answer1} ({time_taken}{parseTime})"))

	submit_code(answer1, '1')

	
	# Data Parsing for part 2
	parseStart = time()
	module.raw_data = data_parser(raw_data)
	parseEnd = time()
	parseTime = (" + " + formatTime(parseEnd - parseStart)) if round(parseEnd - parseStart, 3) > 0 else ""
	# Running Part 2
	with console.status('Running Part 2', spinner='aesthetic'):
		start = time()
		answer2 = module.part2(module.raw_data)
		end = time()
	# print("The answer to the 2nd part is:", answer2)
	time_taken = formatTime(end - start)
	console.print(Panel(f"Answer to the 2nd part: {answer2} ({time_taken}{parseTime})"))

	submit_code(answer2, '2')
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