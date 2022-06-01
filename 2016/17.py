from hashlib import md5

split_data = False
completed = True
raw_data = None # Not To be touched

def hash(password, path):
	return md5((password + path).encode()).hexdigest()

def get_coords(path):
	return ((path.count('U') * -1) + path.count('D')+1, (path.count('L') * -1) + path.count('R')+1)

def get_movements(password, path):
	output = hash(password, path)[:4]
	movements = []
	for direction, key in zip('UDLR', output):
		if key in 'bcdef':
			movements.append(path+direction)
	return movements

def part1(data):
	# Now we just need to find the closest path to (4,4)
	# We can use BFS to find the shortest path
	def bfs(queue):
		new_queue = []
		for path in queue:
			for movement in get_movements(data, path):
				# Check for movement validity
				coords = get_coords(movement)
				if coords == (4,4):
					return movement
				elif 0 < coords[0] <= 4 and 0 < coords[1] <= 4:
					# Make sure that the movement is inbound
					new_queue.append(movement)
		return bfs(new_queue)
	
	return bfs([''])


def part2(data):
	# Instead of finding the shortest path to (4,4), we try to find the longest path to (4,4)
	# We can still use BFS to find the longest path
	valid_paths = []
	def bfs(queue):
		new_queue = []
		for path in queue:
			for movement in get_movements(data, path):
				# Check for movement validity
				coords = get_coords(movement)
				if coords == (4,4):
					# The only change is now we are adding all the possible paths to a list
					valid_paths.append(movement)
				elif 0 < coords[0] <= 4 and 0 < coords[1] <= 4:
					# Make sure that the movement is inbound
					new_queue.append(movement)
		try:
			return bfs(new_queue)
		except RecursionError:
			# Prevents recursion error
			pass
	# Go through all possible paths
	bfs([''])

	# Return the longest path length
	return len(max(valid_paths, key=len))