import re

split_data = True
completed = True
raw_data = None # Not To be touched

bot_cmd = re.compile(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)')
value_cmd = re.compile(r'value (\d+) goes to bot (\d+)')

def proccess_data(data):
	bots = {} # All the bots and their bot functions are in this
	# A simple function that will create the template for the given botID
	def create_bot(id):
		if id not in bots:
			bots[id] = {}
			bots[id]['chips'] = []
			bots[id]['low'] = None
			bots[id]['high'] = None

	for line in data:
		if value_cmd.match(line):
			# If its a value command then give the chip to the bot
			value, bot_id = value_cmd.match(line).groups()
			create_bot(bot_id)
			bots[bot_id]['chips'].append(int(value))
		elif bot_cmd.match(line):
			# If its a bot command then give the instruction to the bot
			bot_id, low_type, low_id, high_type, high_id = bot_cmd.match(line).groups()
			create_bot(bot_id)
			bots[bot_id]['low'] = (low_type, low_id)
			bots[bot_id]['high'] = (high_type, high_id)
	return bots

def part1(data):
	bots = proccess_data(data)
	output_bins = {}

	def process_bot(id):
		bot = bots[id]
		if len(bot['chips']) == 2:
			# Check if the bot has 17 and 61 with it, if yes simply break the loop cause we found our answer
			if min(bot['chips']) == 17 and max(bot['chips']) == 61: return id 
			# Processing the further instructions
			low_type, low_id = bot['low']
			high_type, high_id = bot['high']

			# Deal with diffeerent output types
			# For Low Type
			chip = min(bot['chips'])
			if low_type == 'output':
				# Transfer the chip to the output bin
				output_bins[low_id] = chip
				bot['chips'].remove(chip)
			elif low_type == 'bot':
				# Transfer the chip to the next bot
				bots[low_id]['chips'].append(chip)
				bot['chips'].remove(chip)
				process_bot(low_id) # Recursively process the next bot
			# For High Type
			chip = max(bot['chips'])
			if high_type == 'output':
				# Transfer the chip to the output bin
				output_bins[high_id] = chip
				bot['chips'].remove(chip)
			elif high_type == 'bot':
				# Transfer the chip to the next bot
				bots[high_id]['chips'].append(chip)
				bot['chips'].remove(chip)
				process_bot(high_id) # Recursively process the next bot

	# Now we keep on looping till all the bots have done their task
	while True:
		for bot_id in bots.keys():
			if len(bots[bot_id]['chips']) == 2:
				val = process_bot(bot_id)
				if val: return val # Check if any output is given, if it is then we can return the value

def part2(data):
	# The only difference between part 2 and part 1 are the following
	# The functioning of while loop has changed
	bots = proccess_data(data)
	output_bins = {}

	def process_bot(id):
		bot = bots[id]
		if len(bot['chips']) == 2:
			# Processing the further instructions
			low_type, low_id = bot['low']
			high_type, high_id = bot['high']

			# Deal with diffeerent output types
			# For Low Type
			chip = min(bot['chips'])
			if low_type == 'output':
				# Transfer the chip to the output bin
				output_bins[low_id] = chip
				bot['chips'].remove(chip)
			elif low_type == 'bot':
				# Transfer the chip to the next bot
				bots[low_id]['chips'].append(chip)
				bot['chips'].remove(chip)
				process_bot(low_id) # Recursively process the next bot
			# For High Type
			chip = max(bot['chips'])
			if high_type == 'output':
				# Transfer the chip to the output bin
				output_bins[high_id] = chip
				bot['chips'].remove(chip)
			elif high_type == 'bot':
				# Transfer the chip to the next bot
				bots[high_id]['chips'].append(chip)
				bot['chips'].remove(chip)
				process_bot(high_id) # Recursively process the next bot

	# The loop has been changed because we need a way to break the loop
	# Hence the loop will break once all the bots have done their task
	completed = False
	while not completed:
		completed = True
		for bot_id in bots.keys():
			if len(bots[bot_id]['chips']) == 2:
				completed = False
				process_bot(bot_id)
	return output_bins['0'] * output_bins['1'] * output_bins['2']