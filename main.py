import requests
import importlib

from requests import models
import config
from os import path, makedirs
from time import time

folder_path = f'{config.year}/{config.day}/'
txt_path = f'{config.year}/{config.day}/input.txt'
module_path = f'{config.year}/{config.day}/runner'
raw_data = None

# collect the data
def collect_data(force) -> None:
	"""A simple function to calculate data"""
	global raw_data
	if not path.exists(txt_path) or force:
		response = requests.get(f'https://adventofcode.com/{config.year}/day/{config.day}/input', cookies={'session':config.session_cookie})
		raw_data = response.text.strip()
		# Save the data for backup
		if response.status_code == 200:
			with open(txt_path, 'w') as file:
				file.write(raw_data)
		elif response.status_code == 400 and raw_data == 'Puzzle inputs differ by user.  Please log in to get your puzzle input.':
			print("Hey looks like you need to provide a session cookie!")
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
		makedirs(folder_path)
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
	if not module.completed:
		print("\nWARNING: This answer is still not complete and it may be wrong\n")
	
	# Splitting the data into parts
	if module.split_data == True:
		module.raw_data = raw_data.split('\n')
	elif isinstance(module.split_data, str):
		module.raw_data = raw_data.split(module.split_data)
	else:
		module.raw_data = raw_data

	# Part 1
	start = time()
	answer1 = module.part1(module.raw_data.copy() if isinstance(module.raw_data, list) else raw_data)
	end = time()
	print("The answer to the 1st part is:", answer1)
	# If the total time is above 0.01 secounds then we show it in secounds otherwise we show it in milliseconds
	time_taken = f'{end - start:,.3}s' if end - start > 0.01 else f'{(end - start) * 1000:,.3}ms'
	print(f"The 1st answer was calculated in just {time_taken}")
	# Part 2
	start = time()
	answer2 = module.part2(module.raw_data.copy() if isinstance(module.raw_data, list) else raw_data)
	end = time()
	print("The answer to the 2nd part is:", answer2)
	time_taken = f'{end - start:,.3}s' if end - start > 0.01 else f'{(end - start) * 1000:,.3}ms'
	print(f"The 1st answer was calculated in just {time_taken}")

if __name__ == "__main__":
	if not path.exists(folder_path):
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