split_data = True
completed = True
raw_data = None # Not To be touched

def fuel_calc(num:int) -> int:
	num = int(num)
	fuel = (num // 3) - 2
	return fuel if fuel > 0 else 0

def part1(data):
	# convert data to ints
	# divivde by 3(using // remove decimals) and subtract 2
	# sum all ints
	return sum(map(fuel_calc, data))

def part2(data):
	fuel_sum = 0
	# loop though the data
	for num in data:
		# Convert the mass to int
		num = int(num)
		# Calculate it's fuel
		fuel = fuel_calc(num)
		# Check in a while loop if the fuel is above 0
		while fuel > 0:
			# add the fuel to the sum and set fuel to the required fuel for this fuel
			fuel_sum += fuel
			fuel = fuel_calc(fuel)
	return fuel_sum