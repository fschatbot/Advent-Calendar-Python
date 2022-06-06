split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	return sum(map(int, data))

def part2(data):

	past_freq = [0] # All the past frequencies
	freq = 0 # Current Frequency

	# The below 3 lines help us create the effect of looping through the list again and again
	index = -1
	while True:
		index = (index + 1) % len(data)

		freq += int(data[index]) # Change the Current Frequency

		# Check if the frequency has occured twice, if so, return it, else continue
		if freq in past_freq:
			return freq
		past_freq.append(freq)

