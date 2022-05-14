split_data = False
completed = True
raw_data = None # Not To be touched

def part1(data):
	def isOpenSpace(x, y):
		number = ((x*x) + (3*x) + (2*x*y) + y + (y*y)) + int(data) # This formula is pre-given
		return bin(number)[2:].count('1') % 2 == 0 # return wheter there are even number of 1s in the binary representation of the number
	
	# Use BFS to reach (31, 39)
	def bfs(queue, visited, dept):
		next_queue = [] # The next move to take
		for coord in queue: # For each coordinate in the queue
			for movement in [(coord[0]+1, coord[1]), (coord[0]-1, coord[1]), (coord[0], coord[1]+1), (coord[0], coord[1]-1)]:
				# Loop through all next possible movements for that move
				if movement[0] < 0 or movement[1] < 0 or movement in visited: continue # Make sure to have positive coordinates and are not already visited
				if movement == (31, 39): # If we are at the destination we are done
					return dept
				elif isOpenSpace(*movement): # If the next coordinate is valid
					# We add it to our queue and visited list to make sure we don't come back here
					next_queue.append(movement) 
					visited.append(movement) 
		return bfs(next_queue, visited, dept+1)
	return bfs([(1, 1)], [(1, 1)], 1)


def part2(data):
	# Same as part 1 but instead of a perticular destination we look at the dept
	def isOpenSpace(x, y):
		number = ((x*x) + (3*x) + (2*x*y) + y + (y*y)) + int(data) # This formula is pre-given
		return bin(number)[2:].count('1') % 2 == 0 # return wheter there are even number of 1s in the binary representation of the number
	
	# Use BFS to move around in the maze
	def bfs(queue, visited, dept):
		if dept > 50: return visited
		next_queue = [] # The next move to take
		for coord in queue: # For each coordinate in the queue
			for movement in [(coord[0]+1, coord[1]), (coord[0]-1, coord[1]), (coord[0], coord[1]+1), (coord[0], coord[1]-1)]:
				# Loop through all next possible movements for that move
				if movement[0] < 0 or movement[1] < 0 or movement in visited: continue # Make sure to have positive coordinates and are not already visited
				elif isOpenSpace(*movement): # If the next coordinate is valid
					# We add it to our queue and visited list to make sure we don't come back here
					next_queue.append(movement) 
					visited.append(movement) 
		return bfs(next_queue, visited, dept+1)
	return len(set(bfs([(1, 1)], [(1, 1)], 1)))