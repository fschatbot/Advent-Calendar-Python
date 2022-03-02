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
	# The problem with this program is that it just keeps on repeating itself and finding pairs that are identical but ordered differently
	# The weight of each group
	aim = sum(data) // 3
	groups = remove_dup(find_group(data, aim, []))
	# Find the smallest group length
	glen = len(min(groups, key=lambda x: len(x)))
	# Find all groups with the same length
	smallest_groups = [x for x in groups if len(x) == glen]
	return smallest_groups

def part2(data):
	pass