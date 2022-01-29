import json


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
	# Now that we have proccessed the data into something more readable lets make it into a tree
	# We are sorting the list to make sure that the ones without children come on the top
	# This will allow us the children to be added to the tree

def part1(data):
	_, tree = process_data(data)
	return list(tree.keys())[0]

def part2(data):
	_, tree = process_data(data)
	print(json.dumps(tree, indent=4))