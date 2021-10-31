import itertools

split_data = True
completed = True
raw_data = None # Not To be touched

route_map = {}
destinations = []

def mark_routes(travel_logs):
	for travel_log in travel_logs:
		travel, distance = travel_log.split(' = ')
		ds1, ds2 = travel.split(' to ')
		if ds1 not in destinations:
			destinations.append(ds1)
			route_map[ds1] = {}
		if ds2 not in destinations:
			destinations.append(ds2)
			route_map[ds2] = {}
		route_map[ds1][ds2] = int(distance)
		route_map[ds2][ds1] = int(distance)

def find_distance(*destinations):
	total_distance = 0
	for index, ds in enumerate(destinations[:-1]):
		total_distance += route_map[ds][destinations[index+1]]
	return total_distance

def part1(data):
	"""The Code is supposed to run here"""
	mark_routes(data)
	shortest = find_distance(*destinations)
	for route in itertools.permutations(destinations, len(destinations)):
		des = find_distance(*route)
		if des < shortest:
			shortest = des
	return shortest


def part2(data):
	"""The Code is supposed to run here"""
	longest = find_distance(*destinations)
	for route in itertools.permutations(destinations, len(destinations)):
		des = find_distance(*route)
		if des > longest:
			longest = des
	return longest


def main(puzzle_input):
	global raw_data
	raw_data = puzzle_input
	part1(raw_data.split('\n') if split_data else raw_data)
	part2(raw_data.split('\n') if split_data else raw_data)