import importlib
import inspect
import re
from typing import Callable
import requests
from bs4 import BeautifulSoup

# This file simply generates a file called "completed.md" which contains a table of all the solutions that have been completed

COMPLETED = '✔' # Alternative: ✓
NOT_COMPLETED = '❌'
SEMI_COMPLETED = '½'
NOT_ATTEMPTED = '🚫'

def generate_table(solutions):
	# This will manage the top of the table
	sample_solution = [*solutions.values()]
	days = len(sample_solution[0])
	table = '||' + '|'.join(str(i) for i in range(1, days+1)) + '|\n'
	# Seperator
	table += '|' + '|'.join(['---'] * (days+1)) + '|\n'

	for year, solution in solutions.items():
		table += f'|**{year}**|{"|".join(solution)}|\n'
	
	return table

def isEmpty(func:Callable):
	'''Checks if the function does nothing'''
	source = inspect.getsource(func).split('\n')
	return source[1].strip() in ('pass','...') and len(source) == 3

def check_day(year:int, day:int):
	try:
		module = importlib.import_module(f'{year}.{day}')
	except ModuleNotFoundError:
		return NOT_ATTEMPTED
	if module.completed == True:
		return COMPLETED
	elif module.completed == 1:
		# Only runned if one parts is incomplete
		return SEMI_COMPLETED
	else:
		return NOT_COMPLETED

def get_all_years():
	resp = requests.get('https://adventofcode.com/events')
	soup = BeautifulSoup(resp.text, 'html.parser')
	# Get all the years
	years = [elem.text for elem in soup.find_all('div', class_="eventlist-event")]

	# Getting the year out from the raw text
	match = re.compile(r'\[(\d+)\]')
	years = [match.search(year).groups()[0] for year in years]
	return years

def get_year_completion(year:str):
	# Check all the days from 1 to 25
	solutions = [check_day(year, day) for day in range(1, 26)]
	print(f"Generated solution for year {year}: {' '.join(solutions)}")
	return solutions


def generate_completion():
	years = get_all_years()
	print("Number Of years we are looking: ", len(years))
	solutions = {year: get_year_completion(year) for year in years}
	print("Generated solution status!")
	table = generate_table(solutions)
	print("Generated Solution table!")

	flattened_solutions = []
	for year in solutions.values():
		flattened_solutions += year

	# String That Will be written to the file

	file_text = f'''
## Completion Status

Over Here you can see the completion status of the project.

Parts Completed: {flattened_solutions.count(COMPLETED)*2 + flattened_solutions.count(SEMI_COMPLETED)}/{len(solutions.keys()) * 25 * 2}
<br>
Days Completed: {flattened_solutions.count(COMPLETED)}/{len(solutions.keys()) * 25}

### Legend

- {COMPLETED} = Part Completed
- {SEMI_COMPLETED} = One of the parts have been completed
- {NOT_COMPLETED} = The Day has been attempted but not completed
- {NOT_ATTEMPTED} = Day has not even been attempted

{table}
	'''.strip()

	print("Generated File Text")

	with open('Completed.md', 'w', encoding='utf-8') as f:
		f.write(file_text)
	
	print("Wrote to file!")

if __name__ == '__main__':
	generate_completion()