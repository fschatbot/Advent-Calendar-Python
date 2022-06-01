import numpy as np

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	nums = np.zeros(4294967295+1, dtype=np.bool8)
	for line in data:
		num1, num2 = line.split('-')
		nums[int(num1):int(num2)+1] = True
	return np.where(nums == False)[0][0]

def part2(data):
	nums = np.zeros(4294967295+1, dtype=np.bool8)
	for line in data:
		num1, num2 = line.split('-')
		nums[int(num1):int(num2)+1] = True
	return np.sum(nums == False)