split_data = True
completed = True
raw_data = None # Not To be touched

def isValid(line):
	# A little weird way of getting all the data from the line, but it works
	name = ''.join(line.split('-')[:-1])
	sectorID = int(line.split('-')[-1][:3])
	checksum = line.split('-')[-1][-6:-1]
	letter_count = {}
	for letter in name:
		if letter not in letter_count:
			letter_count[letter] = 1
		else:
			letter_count[letter] += 1
	# Sort the letter based on the amount of times they appear and then on the letter
	# Added benifit of converting it into a list
	sorted_letters = sorted(letter_count.items(), key=lambda x: (-x[1], x[0]))
	# Check if the checksum is correct
	for index, letter in enumerate(checksum):
		if letter != sorted_letters[index][0]:
			break
	else:
		# Not a known fact, but if the loop is not broken, the else statement willl run
		return True

def part1(data):
	sectorIDSum = 0
	for line in data:
		if isValid(line):
			sectorIDSum += int(line.split('-')[-1][:3])
	return sectorIDSum



def part2(data):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'

	for line in data:
		if not isValid(line):continue
		name = '-'.join(line.split('-')[:-1])
		sectorID = int(line.split('-')[-1][:3])

		# Get the new name
		new_name = ''
		for letter in name:
			if letter == '-':
				new_name += ' '
			else:
				new_name += alphabet[(alphabet.index(letter) + sectorID) % 26]
		# Found this by printing the new_name in the console and searching for the word 'north'
		if new_name == 'northpole object storage':
			return sectorID