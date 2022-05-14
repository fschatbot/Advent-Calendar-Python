import numpy as np

split_data = True
completed = True
raw_data = None # Not To be touched

# If I am being honest, this is the most fun challenge
# Easy Code, beautiful output

def part1(data):
	display = np.zeros((6,50), dtype=np.int8)
	for line in data:
		if line.startswith('rect'): # Check if the line is a rect command
			x,y = line.split(' ')[1].split('x') # If yes get all the digits from the command
			# Turn on the display
			display[:int(y),:int(x)] = 1
		elif line.startswith('rotate column'):
			# If the line is a rotate column command
			# Remove the 'column x=' and get the thing after that
			# Then we simply get all the needed numbers
			x,y = line.replace('column x=','').split(' ', maxsplit=1)[1].split(' by ')
			# np.roll rolls the element on a certain axis. Using this function reduces the amount of code to write
			display[:,int(x)] = np.roll(display[:,int(x)],int(y))
		elif line.startswith('rotate row'):
			# Same as above but for rotate row
			x,y = line.replace('row y=','').split(' ', maxsplit=1)[1].split(' by ')
			display[int(x),:] = np.roll(display[int(x),:],int(y))
	return np.sum(display)

def part2(data):
	# Same code from the top
	display = np.zeros((6,50), dtype=np.int8)
	for line in data:
		if line.startswith('rect'):
			x,y = line.split(' ')[1].split('x')
			display[:int(y),:int(x)] = 1
		elif line.startswith('rotate column'):
			x,y = line.replace('column x=','').split(' ', maxsplit=1)[1].split(' by ')
			display[:,int(x)] = np.roll(display[:,int(x)],int(y))
		elif line.startswith('rotate row'):
			x,y = line.replace('row y=','').split(' ', maxsplit=1)[1].split(' by ')
			display[int(x),:] = np.roll(display[int(x),:],int(y))
	# Code for part 2 begins here
	# Printing the display into the console
	display = display.astype(np.str)
	display[display == '1'] = '\u2588' # Full block, makes it easier to read
	display[display == '0'] = ' '
	for row in display:
		print(''.join(row))
	return 'This time, there will be no returned output as its super hard to guess all the letter patterns. However, a human can read the above display and figure out the output!'