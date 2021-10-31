import requests
import importlib

from requests import models
import config
from os.path import exists
from time import time

if not exists(f'{config.year}/{config.day}.txt') or config.force_find:
	response = requests.get(f'https://adventofcode.com/{config.year}/day/{config.day}/input', cookies={'session':config.session_cookie})
	raw_data = response.text.strip()
	# Save the data for backup
	if response.status_code == 200:
		with open(f'{config.year}/{config.day}.txt', 'w') as file:
			file.write(raw_data)
else:
	with open(f'{config.year}/{config.day}.txt', 'r') as file:
		raw_data = ''.join(file.readlines())


# Run the Code
module = importlib.import_module(f'{config.year}.{config.day}')
module.raw_data = raw_data
if not module.completed:
	print("WARNING: This answer is still not complete and it may be wrong")

# Part 1
start = time()
answer1 = module.part1(raw_data.split('\n') if module.split_data else raw_data)
end = time()
print("The answer to the 1st part is:", answer1)
# If the total time is above 0.01 secounds then we show it in secounds otherwise we show it in milliseconds
time_taken = f'{end - start:,.2}s' if end - start > 0.01 else f'{(end - start) * 1000:,.3}ms'
print(f"The 1st answer was calculated in just {time_taken}")
# Part 2
start = time()
answer2 = module.part2(raw_data.split('\n') if module.split_data else raw_data)
end = time()
print("The answer to the 2nd part is:", answer2)
time_taken = f'{end - start:,.2}s' if end - start > 0.01 else f'{(end - start) * 1000:,.3}ms'
print(f"The 1st answer was calculated in just {time_taken}")