split_data = lambda data: [int(x) for x in data.split('\n')]
completed = False
raw_data = None # Not To be touched

def find_group(nums, aim, group):
	groups = []
	for num in nums:
		new_list = nums.copy()
		new_list.remove(num)
		if sum(group) + num == aim:
			# We found a group that works
			groups.append(sorted([*group, num]))
		elif sum(group) + num < aim:
			# We need to keep looking
			new_groups = find_group(new_list, aim, [*group, num])
			if new_groups:
				# print(new_groups)
				groups.extend(new_groups)
		else:
			# We are exceeding the weight
			continue
	return groups

def remove_dup(num_list):
	newk = []
	for i in num_list:
		if i not in newk:
			newk.append(i)
	return newk
		

def part1(data):
	# The weight of each group
	aim = sum(data) // 3
	pairs = remove_dup(find_group(data, aim, []))

def part2(data):
	pass