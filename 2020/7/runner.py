import re

split_data = True
completed = False
raw_data = None # Not To be touched

def proccess_data(data):
	# This is going to be a bit of a mess.
	bags = {}
	for line in data:
		big_bag, other_line = re.fullmatch(r'([\w ]*) bags contain ([\s\S]+).', line).groups()
		if other_line == 'no other bags':
			bags[big_bag] = {}
			continue
		other_bags = other_line.split(', ')
		bag_data = {}
		for bag in other_bags:
			bag_count, bag_name = re.search(r'(\d+) ([\w ]*) bag', bag).groups()
			bag_data[bag_name] = int(bag_count)
		bags[big_bag] = bag_data
	return bags

def looper(lookforbags, bag_data):
	bags = []
	for bag in bag_data:
		# See if a bag from bags exsists in the current bag if it does, add it to the list.
		if any(lookforbag in bag_data[bag] for lookforbag in lookforbags):
			bags.append(bag)
	new_bags = list(set(bags))
	bags = list(set(lookforbags))
	# if the list given is the same as the list of bags, we have found the end. Then we have found the answer
	# The -1 is to eleminate the shiny gold bag.
	if len(new_bags) == len(bags) - 1:
		return len(bags) - 1
	else:
		return looper(list(set([*lookforbags, *new_bags])), bag_data)

def part1(data):
	# This one is going to be hard to do.
	bag_data = proccess_data(data)
	return looper(['shiny gold'], bag_data)
	

def find_bags(bag, bag_data):
	total = 0
	bag_content = bag_data[bag]
	# We go though each bag in the bag_content and add the number of bags in the bag to the total.
	for bag_name, count in bag_content.items():
		total += count +  (count * find_bags(bag_name, bag_data))
	return total


def part2(data):
	bag_data = proccess_data(data)
	return find_bags('shiny gold', bag_data)
