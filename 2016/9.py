import re

split_data = False
completed = True
raw_data = None # Not To be touched

def part1(data):
	decompressed_output = ''
	pointer = 0
	while pointer < len(data):
		if data[pointer] not in '(':
			# The data is not a marker, so continue like normal
			decompressed_output += data[pointer]
			pointer += 1
		else:
			# We have reached a marker...
			match = re.match(r'\((\d+)x(\d+)\)', data[pointer:])
			till, repeat = match.groups() # Get the length of the marker and the number of times to repeat
			marker_end_index = pointer + match.end() # Get the index of where the marker ends
			decompressed_output += data[marker_end_index:marker_end_index + int(till)] * int(repeat) # Simple decompression
			pointer = marker_end_index + int(till) # Update the pointer to the end of the decompressed data
	return len(decompressed_output)

def decompress(string):
	decompresion_length = 0
	pointer = 0
	while pointer < len(string):
		if string[pointer] not in '(':
			# The data is not a marker, so continue like normal
			decompresion_length += 1
			pointer += 1
		else:
			# We have reached a marker...
			match = re.match(r'\((\d+)x(\d+)\)', string[pointer:])
			till, repeat = match.groups() # Get the length of the marker and the number of times to repeat
			marker_end_index = pointer + match.end() # Get the index of where the marker ends
			decompresion_length += decompress(string[marker_end_index:marker_end_index + int(till)]) * int(repeat) # Simple decompression
			pointer = marker_end_index + int(till) # Update the pointer to the end of the decompressed data
	return decompresion_length

def part2(data):
	# Another way we can do this is by taking the string we need to repeat and putting it through decompression
	# Then we can take the string we are going to multiple and put it through decompression again
	# This will create a recurrsion that will eventually end when the we decompress a string entirely
	# Then we will multiple the decompressed string by the number of times we need to repeat it
	# This is exactly what we did in part 1 but now with recurrsion
	return decompress(data)
