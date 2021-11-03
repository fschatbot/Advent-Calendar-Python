split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	paper_needed = 0
	for line in data:
		l, w, h = [int(x) for x in line.split('x')]
		SAarea = 2*l*w + 2*w*h + 2*h*l
		min_side = min(l*w, w*h, h*l)
		paper_needed += SAarea + min_side
	return paper_needed

def part2(data):
	ribon_needed = 0
	for line in data:
		l, w, h = [int(x) for x in line.split('x')]
		bow = l*w*h
		wrapping = min(2*l + 2*w, 2*h + 2*w, 2*h + 2*l)
		ribon_needed += bow + wrapping
	return ribon_needed