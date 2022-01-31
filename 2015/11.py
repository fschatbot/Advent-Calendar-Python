import re

split_data = False
completed = True
raw_data = None # Not To be touched

# The string does not contain i,o,l as they will be skipped anyways
safe_letters = 'abcdefghjkmnpqrstuvwxyz'
# This creates strings like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
combi = [a+b+c for a,b,c in zip('abcdefghijklmnopqrstuvwx', 'bcdefghijklmnopqrstuvwxy', 'cdefghijklmnopqrstuvwxyz')]
prev_password = None

def check_pass(password):
	# The first Checks if the length of the password is 8
	# The first check is for if any of the combi are in the password
	# The secound checks if least two different, non-overlapping pairs of letters
	return any(x in password for x in combi) == True and re.search(r'(.)\1.*(.)\2', password) != None

def next_pass(password, i=7):
	# This is the most complicated thing but let me explain it:
	# The i represents 7 as in the last letter of the password
	# The nextletter basically gets the the index of the next letter in the safe_letters string
	next_letter = safe_letters.index(password[i])+1
	# If the next letter is bigger than total possible combination than we set the letter being delt with to a
	if next_letter >= len(safe_letters):
		# Next we run the next pass function with the previous letter
		password = password[:i] + safe_letters[0] + password[i+1:]
		return next_pass(password, i-1)
	# if not then send the password with the next letter
	return password[:i]+ safe_letters[next_letter]+password[i+1:]

def part1(data):
	global prev_password
	password = data
	while not check_pass(password):
		password = next_pass(password)
	prev_password = password
	return password

def part2(data):
	password = next_pass(prev_password)
	while not check_pass(password):
		password = next_pass(password)
	return password