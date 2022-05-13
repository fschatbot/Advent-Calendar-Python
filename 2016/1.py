split_data = ','
completed = True
raw_data = None # Not To be touched

def part1(data):
	facing = 0 # 0 = North, 1 = East, 2 = South, 3 = West
	coords = [0, 0]
	visited = [[0, 0]] # Only for CSV
	
	for step in data:
		# Update the facing direction
		if step.startswith('R'):
			facing = (facing + 1) % 4
		elif step.startswith('L'):
			facing = (facing - 1) % 4
		# Update the coords
		if facing == 0:
			coords[1] += int(step[1:])
		elif facing == 1:
			coords[0] += int(step[1:])
		elif facing == 2:
			coords[1] -= int(step[1:])
		elif facing == 3:
			coords[0] -= int(step[1:])
		visited.append(coords.copy()) # Only for CSV
	# Open the csv and copy paste the data in desmos. It will help you visualize the data
	csv = '\n'.join(','.join(str(i) for i in x) for x in visited)
	with open('2016/day 1 - step dump.csv', 'w') as file:
		file.write(csv)
	
	return abs(coords[0]) + abs(coords[1])

def part2(data):
	facing = 0 # 0 = North, 1 = East, 2 = South, 3 = West
	coords = [0, 0]
	visited = [[0, 0]]

	for step in data:
		prev_coord = coords.copy()
		# Update the facing direction
		if step.startswith('R'):
			facing = (facing + 1) % 4
		elif step.startswith('L'):
			facing = (facing - 1) % 4
		
		# Update the coords
		if facing == 0:
			coords[1] += int(step[1:])
		elif facing == 1:
			coords[0] += int(step[1:])
		elif facing == 2:
			coords[1] -= int(step[1:])
		elif facing == 3:
			coords[0] -= int(step[1:])

		steps = []
		# Add all the coordinates between the previous and current coords

		if prev_coord[0] == coords[0]:
			for y in range(prev_coord[1], coords[1], 1 if prev_coord[1] < coords[1] else -1):
				steps.append([prev_coord[0], y])
		elif prev_coord[1] == coords[1]:
			for x in range(prev_coord[0], coords[0], 1 if prev_coord[0] < coords[0] else -1):
				steps.append([x, prev_coord[1]])
		else:
			print("How did we get here?")
		# Check if any of the steps coords are there in the visited list
		for step in steps[1:]: # Not checking the first one because its bound to be in the list
			if step in visited:
				return abs(step[0]) + abs(step[1])
		# If not then add them to the visited list
		visited.extend(steps)
		
	return abs(coords[0]) + abs(coords[1]) # We should never get here