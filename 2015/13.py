import itertools
import re

split_data = True
completed = True
raw_data = None # Not To be touched

chart = {}
members = []

def mark_chart(data):
	global members
	regx = r'(\w+) would ([\w]+) (\d+) happiness units by sitting next to (\w+).'
	for line in data:
		name1, multiplier, amount, name2 = re.fullmatch(regx, line).groups()
		members.extend((name1,name2)) # add all the names to the groups
		# In case these names are not registered, register them
		if name1 not in chart:
			chart[name1] = {}
		# the happiness meter in the chart
		amount = int(amount)
		chart[name1][name2] = amount * (-1 if multiplier == 'lose' else 1)
	# remove all the names that have been repeated
	members = list(set(members))

def calculate_happiness(*member_names):
	happiness = 0
	for index, member in enumerate(member_names):
		# First Level Happiness
		i = (index - 1 + len(member_names)) % len(member_names)
		happiness += chart[member][member_names[i]]
		# Second Level Happiness
		# What this does is if the next index is out of range it wraps it back to 1
		i = (index + 1 + len(member_names)) % len(member_names)
		happiness += chart[member][member_names[i]]
	return happiness

def part1(data):
	"""The Code is supposed to run here"""
	mark_chart(data)
	optimal_happiness = calculate_happiness(*members)
	for arrangment in itertools.permutations(members, len(members)):
		happiness = calculate_happiness(*arrangment)
		if happiness > optimal_happiness:
			optimal_happiness = happiness
	return optimal_happiness


def part2(data):
	"""The Code is supposed to run here"""
	mark_chart(data)
	# Go though the list and add your self
	for key in chart.keys():
		chart[key]['me'] = 0
	chart['me'] = {}
	for key in chart.keys():
		chart['me'][key] = 0
	members.append('me')
	# Calculate the best Happiness
	optimal_happiness = calculate_happiness(*members)
	for arrangment in itertools.permutations(members, len(members)):
		happiness = calculate_happiness(*arrangment)
		if happiness > optimal_happiness:
			optimal_happiness = happiness
	return optimal_happiness