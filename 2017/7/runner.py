from ctypes import Union
import json
from typing import List

split_data = True
completed = False
raw_data = None # Not To be touched

# This cache is the ultimate tree
cache = {}

def proccess_children(children, data):
	# First we create a dict which is going to be returned
	new_children = {}
	# We loop through each child getting their name
	for child in children:
		# We check if the child has already been proccessed and is stored in the cache
		if child in cache:
			# If it has we add it to the new_children dict and remove it from the cache
			new_children[child] = cache[child]
			# Remove it from the cache to save mem
			del cache[child]
		else:
			# If no then we might have to do it on our own
			# First check if there are any children
			if data[child]['children']:
				# If yes then proccess them and replace the simply arr with the new dict
				data[child]['children'] = proccess_children(data[child]['children'], data)
			# Next add the final data to the new_children dict
			new_children[child] = data[child]
			# Delete the child we just proccessed from the list to prevent it from being proccessed again
			del data[child]
	return new_children
	

def process_data(data):
	# This just converts the data into a readable flatmap by the program
	new_data = {}
	for line in data:
		name = line.split(" (")[0]
		weight = int(line.split(" (")[1].split(")")[0])
		children = line.split(" -> ")[1].split(", ") if "->" in line else []
		new_data[name] = {
			"weight": weight,
			"children": children
		}
	# Over here we convert the data into a tree
	# We loop through the copy of the data to prevent changing errors
	for name, value in new_data.copy().items():
		# If the child has been deleted it means it has been proccessed so we skip it
		if name not in new_data: continue
		# Next we add the info into the cache to save time in the future
		cache[name] = value
		# If the child has children we proccess their children
		if value['children']:
			cache[name]['children'] = proccess_children(value['children'], new_data)
		# Next we remove the child from the data list to save mem
		del new_data[name]
	# Make a copy and clear the cache so it can be procesed again
	tree = cache.copy()
	cache.clear()
	return new_data, tree

def part1(data):
	_, tree = process_data(data)
	return list(tree.keys())[0]

def FindTheOddOneOut(arr):
	# Count how many times a number appears in the array
	counter = {}
	for i in arr:
		if sum(i) in counter:
			counter[sum(i)] += 1
		else:
			counter[sum(i)] = 1
	# Find the number that appears only once
	for num,value in counter.items():
		if value == 1:
			# This returns the number that appears only once and the one other number as sample
			return num, [name for name in counter.keys() if name != num][0]
	else:
		return None

def collapes_tower(tower_value):
	"""
	This function takes in the tower dict and returns 2 values

	1. (The weight of the tower, The total weight of the children) or int

	> Situation 1: The values are not added up but returned as a tuple. Ex: (int, int)
	> Situation 2: The value returned is the answer
	
	2. Boolean

	> If this is true then it means that the data returned above is the answer and should we handded down the tree instantly
	"""
	# If there are no children then we just return the weight
	if not tower_value['children']: return (tower_value['weight'], 0), False

	# This for loop gets the weight of each child in a list
	children = tower_value['children'].copy()
	tower_value['children'] = []
	for value in children.values():
		weight, true_return = collapes_tower(value)
		# A true return means it is the answer to our problem
		# Hence we skip everything else and return it down the tree and back to the part1 as fast as possible
		# However if we don't get a true return we simply replace the child with it's weight
		if true_return: return weight
		else: tower_value['children'].append(weight)
	# Next we compare to see if the children have the same weight, If not then boom we found the problem
	odd_one = FindTheOddOneOut(tower_value['children'])
	if odd_one:
		# Now we need to find which child is the odd one out
		unbalanced_child = [child for child in tower_value['children'] if sum(child) == odd_one[0]][0]
		# This returns the differnce in weight between the odd one and the other child
		diff = odd_one[1] - sum(unbalanced_child)
		# We combine the difference and we get our answer which we pass down the tree
		print(unbalanced_child[0] + diff)
		return unbalanced_child[0] + diff, True
	else:
		# Return the weight of the children plus the inital weight of the tower and false
		return (tower_value['weight'], sum(sum(child) for child in tower_value['children'])), False

def part2(data):
	_, tree = process_data(data)
	# We have to loop through each tower and essitally collapsing the children to get the total weight of the towers
	tower_weight, _ = collapes_tower(tree[list(tree.keys())[0]])
	return tower_weight