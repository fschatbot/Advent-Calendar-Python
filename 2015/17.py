split_data = True
completed = True
raw_data = None # Not To be touched

from functools import cache			

def part1(data):
	"""The Code is supposed to run here"""
	containers = sorted([int(container) for container in data], reverse=True)

	@cache
	def try_fitting(remaining:int, index:int):
		if remaining == 0:
			return 1
		elif remaining < 0 or index >= len(containers):
			return 0 # We ran out of containers and still didn't achieve our goals
		
		use_it = try_fitting(remaining - containers[index], index+1) # We either use this container
		no_use = try_fitting(remaining, index+1) # or we don't use it. 

		# If the current container consumes too much, then it will automaticlly return 0
		return use_it + no_use
		
	return try_fitting(150, 0)

def part2(data):
	"""The Code is supposed to run here"""
	containers = [int(container) for container in data]

	@cache
	def try_fitting(remaining:int, index:int, counter:int):
		if remaining == 0:
			return counter, 1
		elif remaining < 0 or index >= len(containers):
			return float('inf'), 0 # We ran out of containers and still didn't achieve our goals
		
		use_it = try_fitting(remaining - containers[index], index+1, counter+1) # We either use this container
		no_use = try_fitting(remaining, index+1, counter) # or we don't use it.

		if use_it[0] < no_use[0]:
			return use_it
		elif use_it[0] > no_use[0]:
			return no_use
		else:
			return use_it[0], use_it[1] + no_use[1]
	
	return try_fitting(150, 0, 0)[1]