import requests
import importlib
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
start = time()
answer1 = module.part1(raw_data.split('\n') if module.split_data else raw_data)
print("The answer to the 1st part is:", answer1)
print(f"The 1st answer was calculated in just {(time() - start) * 1000:,.3}ms")
start = time()
answer2 = module.part2(raw_data.split('\n') if module.split_data else raw_data)
print("The answer to the 2nd part is:", answer2)
print(f"The 2nd answer was calculated in just {(time() - start) * 1000:,.3}ms")