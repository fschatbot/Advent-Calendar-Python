split_data = lambda data: sorted([int(x) for x in data.split('\n')], reverse=True)
completed = True
raw_data = None # Not To be touched

from functools import cache

def part1(data):
	aim = sum(data) // 3

	@cache
	def pruned_packing(index, gp, best_gp, best_QE):
		if index == len(data):
			# We have reached base case.
			if all(gp[i] == aim for i in range(3)) and (gp[3] < best_gp or (gp[3] == best_gp and gp[4] < best_QE)):
				return gp[3], gp[4]
			else:
				return best_gp, best_QE


		# Group = [gp_0 sum, gp_1 sum, gp_2 sum, gp_0 len, gp_0 QE]
		# index = index of the package we are currently processing

		if gp[3] < best_gp and gp[0] + data[index] <= aim and not (gp[3]+1 == best_gp and gp[4] * data[index] > best_QE): # Only check if the current has the potential to be better
			ngp = (gp[0] + data[index], gp[1], gp[2], gp[3] + 1, gp[4] * data[index])
			best_gp, best_QE = pruned_packing(index+1, ngp, best_gp, best_QE)
		
		# See if we can add to the current grouping...
		for group in range(1, 3):
			if gp[group] + data[index] > aim: continue # No need to consider
			if gp[group] == gp[group-1]: continue # Adding here would make no difference
			ngp = list(gp)
			ngp[group] += data[index] # Add the gift to the bag
			ngp[1:3] = sorted(ngp[1:3])
			best_gp, best_QE = pruned_packing(index+1, tuple(ngp), best_gp, best_QE)
		
		return best_gp, best_QE
	
	return pruned_packing(0, (0, 0, 0, 0, 1), float('inf'), float('inf'))[1]


def part2(data):
	aim = sum(data) // 4

	@cache
	def pruned_packing(index, gp, best_gp, best_QE):
		if index == len(data):
			# We have reached base case.
			if all(gp[i] == aim for i in range(4)) and (gp[4] < best_gp or (gp[4] == best_gp and gp[5] < best_QE)):
				return gp[4], gp[5]
			else:
				return best_gp, best_QE


		# Group = [gp_0 sum, gp_1 sum, gp_2 sum, gp_3 sum, gp_0 len, gp_0 QE]
		# index = index of the package we are currently processing

		if gp[4] < best_gp and gp[0] + data[index] <= aim and not (gp[4]+1 == best_gp and gp[5] * data[index] > best_QE): # Only check if the current has the potential to be better
			ngp = (gp[0] + data[index], gp[1], gp[2], gp[3], gp[4] + 1, gp[5] * data[index])
			best_gp, best_QE = pruned_packing(index+1, ngp, best_gp, best_QE)
		
		# See if we can add to the current grouping...
		for group in range(1, 4):
			if gp[group] + data[index] > aim: continue # No need to consider
			if gp[group] == gp[group-1]: continue # Adding here would make no difference
			ngp = list(gp)
			ngp[group] += data[index] # Add the gift to the bag
			ngp[1:4] = sorted(ngp[1:4])
			best_gp, best_QE = pruned_packing(index+1, tuple(ngp), best_gp, best_QE)
		
		return best_gp, best_QE
	
	return pruned_packing(0, (0, 0, 0, 0, 0, 1), float('inf'), float('inf'))[1]