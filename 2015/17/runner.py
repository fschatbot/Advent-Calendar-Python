split_data = True
completed = False
raw_data = None # Not To be touched

coms = 0

def loop(canfit, containers, listing=[]):
	global coms
	for container in containers:
		if container == canfit:
			print([*listing, container])
			coms += 1
		elif container < canfit:
			list2 = containers.copy()
			list2.remove(container)
			loop(canfit - container, list2, [*listing, container])

def part1(data):
	"""The Code is supposed to run here"""
	containers = [int(container) for container in data]
	loop(25, containers)
	return coms

def part2(data):
	"""The Code is supposed to run here"""
	containers = [int(container) for container in data]