#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(data):
	return [int(x) for x in data]

split_data = parse
completed = True
raw_data = None # Not To be touched

def part1(data):
	fileSystem = [None] * sum(data)

	# Populate the fileSystem
	i = 0
	for id, block in enumerate(data):
		if id % 2 == 0: # Every odd one is block
			fileSystem[i:i+block] = [id // 2]*block # Simple ID calculation
		i += block
	
	# Printing the fileSystem
	# print(''.join(str(x) if x is not None else '.' for x in fileSystem))

	# Run the compacting proccess
	left = 0
	right = len(fileSystem) - 1

	while left < right:
		if fileSystem[left] is None and fileSystem[right] is None:
			right -= 1
		elif fileSystem[left] is None and fileSystem[right] is not None:
			fileSystem[left] = fileSystem[right]
			fileSystem[right] = None
			# These two lines are unncecary but still help in optimization
			right -= 1
			left += 1
		elif fileSystem[left] is not None:
			left += 1
		# print(''.join(str(x) if x is not None else '.' for x in fileSystem))

	return sum(index * id for index, id in enumerate(fileSystem[:left]))

def part2(data):
	# Instead of using a ram array. We should instead just keep an array of file blocks

	files = []
	for id, block in enumerate(data):
		files.append({
			'type': 'file' if id % 2 == 0 else 'free',
			'size': block,
			'id': id // 2 if id % 2 == 0 else '.' # For free blocks, we simply ignore this "id"
		})
	
	# print(len(files))

	for fi in range(len(files) - 1, -1, -1):
		file = files[fi]
		if file['type'] == 'free': continue

		for bi in range(len(files)):
			block = files[bi]
			if block['type'] == 'file' and block['id'] == file['id']: break # Only check the left side
			if block['type'] == 'file': continue # We don't care about files
			if block['size'] < file['size']: continue # This free space is too small

			# We are looking at a block which can fit the file...
			block['size'] -= file['size']
			files.insert(bi, files.pop(fi)) # Reposition
			files.insert(fi, {
				'type': 'free',
				'size': file['size'],
				'id': '.'
			}) # Adding a free space in it's place
			break
	
	cum = 0
	index = 0
	for f in files:
		if f['type'] == 'file':
			for i in range(f['size']):
				cum += (i+index) * f['id']
		index += f['size']
	
	return cum







	
	

