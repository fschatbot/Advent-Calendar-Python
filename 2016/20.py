import numpy as np

def parse(data):
	processed = []
	for line in data.strip().split('\n'):
		num1, num2 = line.split('-')
		processed.append((int(num1), int(num2)))
	
	return sorted(processed, key=lambda x: x[0])

split_data = parse
completed = True
raw_data = None # Not To be touched

def part1(data):
	lowest = 0

	for low, high in data:
		if low <= lowest <= high:
			lowest = high + 1
	
	return lowest

def part2(data):
	allowedRange = [(0, 4294967295)]

	for low, high in data:
		newRange = []
		for Al_low, Al_high in allowedRange:
			if Al_low < low and Al_high > high:
				# The middle part of the range is in the black-list
				newRange.append((Al_low, low-1))
				newRange.append((high+1, Al_high))
			elif low <= Al_low <= high:
				# The lower part of the range is in the black-list
				if Al_high <= high:
					# Then the whole range is in the black-list
					continue
				else:
					# The above part of the range is not in the black-list
					newRange.append((high+1, Al_high))
			elif low <= Al_high <= high:
				# The above part of the range is in the black-list
				if Al_low < low:
					# The below part of the range is not in blacklist
					newRange.append((Al_low, low-1))
				else:
					# The below part of the range is in the black-list
					continue
			else:
				# The whole range is not in the black-list
				newRange.append((Al_low, Al_high))
		
		allowedRange = newRange
		if len(allowedRange) == 0:
			break
	
	return sum([high - low + 1 for low, high in allowedRange])