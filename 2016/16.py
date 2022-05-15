from tabnanny import check


split_data = False
completed = True
raw_data = None # Not To be touched

def encode(data):
	# Encoding the data using modified Dragon Checksum
	a = data
	b = a[::-1]
	b = b.replace('0', 'x').replace('1', '0').replace('x', '1')
	return f'{a}0{b}'

def generate_checksum(data):
	# Generating the checksum
	checksum = ''
	for i in range(0, len(data), 2):
		checksum += '1' if data[i] == data[i+1] else '0'
	# Check wheter the length of checksum is even
	if len(checksum) % 2 == 0:
		return generate_checksum(checksum)
	else:
		return checksum

def part1(data):
	while len(data) < 272: data = encode(data) # encoding till the length is 272
	data = data[:272]	
	return generate_checksum(data)

def part2(data):
	while len(data) < 35651584: data = encode(data) # encoding till the length is 272
	data = data[:35651584]	
	return generate_checksum(data)