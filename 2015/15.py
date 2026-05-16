import re, json

def process_data(data):
	regx = r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)'
	for line in data.split('\n'):
		name, capacity, durability, flavor, texture, calories = re.fullmatch(regx, line).groups()
		chart[name] = {'capacity': int(capacity), 'durability': int(durability), 'flavor':int(flavor), 'texture':int(texture), 'calories':int(calories)}

split_data = process_data
completed = True
raw_data = None # Not To be touched

chart = {}


def get_score(*args):
	configs = [*chart.values()]
	final_score = 1
	for key in ['capacity', 'durability', 'flavor', 'texture']:
		final_score *= max(0, sum(ingredient[key] * count for ingredient, count in zip(configs, args)))
	return final_score

def part1(data):
	"""The Code is supposed to run here"""
	highest_score = 0
	# Using this method is slow but still it's possible to solve the question like so
	for fros in range(1, 100):
		for cand in range(100-fros, 1, -1):
			for butter in range(100-fros-cand, 1, -1):
				sugar = 100 - fros - cand - butter
				# The Highest Score will be now the best one between this two
				highest_score = max(highest_score, get_score(fros, cand, butter, sugar))
	return highest_score


def part2(data):
	"""The Code is supposed to run here"""
	highest_score = 0
	# Using this method is slow but still it's possible to solve the question like so
	for fros in range(1, 100):
		for cand in range(100-fros, 1, -1):
			for butter in range(100-fros-cand, 1, -1):
				sugar = 100 - fros - cand - butter

				# Calculing the calories
				calories = sum(ingredient['calories'] * count for ingredient, count in zip(chart.values(), [fros, cand, butter, sugar]))
				if calories != 500: continue

				# The Highest Score will be now the best one between this two
				highest_score = max(highest_score, get_score(fros, cand, butter, sugar))
	return highest_score