import re, json

split_data = True
completed = False
raw_data = None # Not To be touched

speed_map = {}

def mark_chart(data):
	regx = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'
	for line in data:
		name, speed, duration, rest_duration = re.fullmatch(regx, line).groups()
		speed_map[name] = {
			'speed': int(speed), 
			'speed_duration':int(duration),
			'rest_duration':int(rest_duration),
			'resting':False,
			'duration': int(duration),
			'distance': 0,
			'points': 0
		}

def simiulate_seconds():
	for _ in range(2503):
		for deer, config in speed_map.items():
			if config['resting'] == True and config['duration'] != 0:
				# The deer is resting and the time period is still going
				pass
			elif config['resting'] == False and config['duration'] != 0:
				# The deer is not resting and the time period is still going
				speed_map[deer]['distance'] += config['speed']
			elif config['resting'] == True and config['duration'] <= 0:
				# The deers rest is over and it has started running
				speed_map[deer]['duration'] = config['speed_duration']
				speed_map[deer]['resting'] = False
				speed_map[deer]['distance'] += config['speed']
			elif config['resting'] == False and config['duration'] <= 0:
				# The deers rest is over and it has started running
				speed_map[deer]['duration'] = config['rest_duration']
				speed_map[deer]['resting'] = True
			else:
				# Incase something messes up (Please create a report and I will look into it)
				print("IDK how we reached here??\nDeer:",deer,"\nConfig:",config,"\nTime:",_)
			speed_map[deer]['duration'] -= 1
		# Award 1 point to the furthest deer {part 2}
		furthest = max(config['distance'] for config in speed_map.values())
		for deer, config in speed_map.items():
			if config['distance'] == furthest:
				speed_map[deer]['points'] += 1

def part1(data):
	"""The Code is supposed to run here"""
	mark_chart(data) # Gather the data and make a chart
	simiulate_seconds() # Simiulate the seconds
	# Now we use max to find the furthest distance
	# The list passed is just the final distances travelled by the raindeers
	return max(config['distance'] for config in speed_map.values())


def part2(data):
	"""The Code is supposed to run here"""
	mark_chart(data)
	simiulate_seconds()
	# This time we look for the max points instead of distance
	return max(config['points'] for config in speed_map.values())