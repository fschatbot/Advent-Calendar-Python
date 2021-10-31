split_data = True
completed = True
raw_data = None # Not To be touched

circut = {}
ans1 = None

def is_num(str):
	try:
		int(str)
		return True
	except TypeError:
		return False
	except ValueError:
		return False

def processer(process):
	if process.startswith('NOT'):
		data = {'op': '~', 'val1': process[4:]}
	elif 'AND' in process:
		val1, val2 = process.split(' AND ')
		data = {'op': '&', 'val1': val1, 'val2': val2}
	elif 'OR' in process:
		val1, val2 = process.split(' OR ')
		data = {'op': '|', 'val1': val1, 'val2': val2}
	elif 'LSHIFT' in process:
		val1, val2 = process.split(' LSHIFT ')
		data = {'op': '<<', 'val1': val1, 'val2': int(val2)}
	elif 'RSHIFT' in process:
		val1, val2 = process.split(' RSHIFT ')
		data = {'op': '>>', 'val1': val1, 'val2': int(val2)}
	else:
		data = process
	return data

def finder(to_find):
	if is_num(to_find):
		return int(to_find)
	
	data = circut[to_find]
	if is_num(data):
		return int(data)
	elif isinstance(data, str):
		return finder(data)
	elif data['op'] == '~':
		val = ~finder(data['val1'])
		circut[to_find] = val
		return val
	elif data['op'] == '&':
		val = finder(data['val1']) & finder(data['val2'])
		circut[to_find] = val
		return val
	elif data['op'] == '|':
		val = finder(data['val1']) | finder(data['val2'])
		circut[to_find] = val
		return val
	elif data['op'] == '<<':
		val = finder(data['val1']) << data['val2']
		circut[to_find] = val
		return val
	elif data['op'] == '>>':
		val = finder(data['val1']) >> data['val2']
		circut[to_find] = val
		return val

def part1(data):
	"""The Code is supposed to run here"""
	global circut, ans1
	# Put in process
	for bit in data:
		process, output = bit.split(' -> ')
		circut[output.strip()] = processer(process.strip())
	ans1 = finder('a') # Set the first answer as global so it can be used later
	return ans1

def part2(data):
	global circut
	# Proccess the data
	for bit in data:
		process, output = bit.split(' -> ')
		circut[output.strip()] = processer(process.strip())
	# Replace b with the previous answer
	circut['b'] = ans1
	return finder('a')
