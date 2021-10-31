split_data = True
raw_data = None # Not To be touched

circut = {}

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

def runner(data):
	"""The Code is supposed to run here"""
	global circut
	# Put in process
	for bit in data:
		process, output = bit.split(' -> ')
		circut[output.strip()] = processer(process.strip())
	circut_copy = circut.copy() # Make A first Copy
	answer = finder('a')
	print("Answer To First Part:", answer)
	circut = circut_copy.copy() # Restore that copy
	circut['b'] = answer
	answer = finder('a')
	print("Answer To Second Part:", answer)

def main(puzzle_input):
	global raw_data
	raw_data = puzzle_input
	runner(raw_data.split('\n') if split_data else raw_data)
