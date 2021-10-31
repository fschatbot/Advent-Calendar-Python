import re, json

split_data = True
completed = False
raw_data = None # Not To be touched

chart = {}

def process_data(data):
	regx = r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)'
	for line in data:
		name, capacity, durability, flavor, texture, calories = re.fullmatch(regx, line).groups()
		chart[name] = {'capacity': int(capacity), 'durability': int(durability), 'flavor':int(flavor), 'texture':int(texture), 'calories':int(calories)}

def get_score(*args):
	configs = [*chart.values()]
	capacity_score = sum(
		# chart.values()[index]	will give us the configuration for the corresponding ingredient
		# args[index]			will gives us how many times is the ingredient used
		configs[index]['capacity'] * args[index] 
		for index in range(len(args))
	)
	durability_score = sum(configs[index]['durability'] * args[index] for index in range(len(args)))
	flavor_score = sum(configs[index]['flavor'] * args[index] for index in range(len(args)))
	texture_score = sum(configs[index]['texture'] * args[index] for index in range(len(args)))
	
	final_score = capacity_score * durability_score * flavor_score * texture_score
	return final_score

def part1(data):
	"""The Code is supposed to run here"""
	process_data(data)
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
	process_data(data)