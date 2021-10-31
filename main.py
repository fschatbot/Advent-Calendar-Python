import requests
import importlib
import config
from os.path import exists


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
key = importlib.import_module(f'{config.year}.{config.day}')
key.main(raw_data)