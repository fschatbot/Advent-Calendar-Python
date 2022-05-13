from hashlib import md5

split_data = False
completed = True
raw_data = None # Not To be touched

def part1(data):
	password = ''
	for i in range(9999999999):
		# Run the string through md5
		encoded = md5((data+str(i)).encode('utf-8')).hexdigest()
		# Check for 5 leading zeros
		if encoded[:5] == '00000':
			# Add the letter to the password
			password += encoded[5]
			# Check if we have the correct length and return the password
			if len(password) == 8:
				return password

def part2(data):
	password = [''] * 8
	for i in range(9999999999):
		# Run the string through md5
		encoded = md5((data+str(i)).encode('utf-8')).hexdigest()
		# Check for 5 leading zeros
		if encoded[:5] == '00000':
			# Check for valid index
			try:
				index = int(encoded[5])
			except ValueError:
				continue
			if index < 8 and password[index] == '':
				# Add the letter to the password
				password[index] = encoded[6]
			# Check if we have the correct length and return the password
			if '' not in password:
				return ''.join(password)
