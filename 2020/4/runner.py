import re

split_data = '\n\n'
completed = True
raw_data = None # Not To be touched

def process_data(passports):
	new_passports = []
	for passport in passports:
		new_passport_str = passport.replace('\n' ,' ')
		new_passport = {}
		for detail in new_passport_str.split(' '):
			key, value = detail.split(':')
			new_passport[key] = value
		new_passports.append(new_passport)
	return new_passports
		

def part1(data):
	passports = process_data(data)
	# cid is skipped for now
	required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	valid_passports = 0
	for passport in passports:
		# We look for if the required keys are in the passport
		if set(required_keys).issubset(passport.keys()):
			valid_passports += 1
	return valid_passports

def part2(data):
	match_data = {
		'byr': lambda amount: 1920 <= int(amount) <= 2002,
		'iyr': lambda amount: 2010 <= int(amount) <= 2020,
		'eyr': lambda amount: 2020 <= int(amount) <= 2030,
		'hgt': lambda amount: (amount.endswith('cm') and 150 <= int(amount[:-2]) <= 193) or (amount.endswith('in') and 59 <= int(amount[:-2]) <= 76),
		'hcl': lambda amount: not not re.match('#[0-9a-f]{6}', amount),
		'ecl': lambda amount: amount in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
		'pid': lambda amount: not not re.fullmatch('[0-9]{9}', amount),
		'cid': lambda amount: True
	}
	required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	passports = process_data(data)
	valid_passports = 0
	for passport in passports:
		# Make sure it still has all the keys
		if set(required_keys).issubset(passport.keys()):
			# if the data is invalid then the loop will break and if it doesn't then the passport is valid
			for key, value in passport.items():
				if not match_data[key](value.strip()):
					# The passport is invalid
					break
			else:
				# The passport is valid
				valid_passports += 1
	return valid_passports