#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = ' '
completed = True
raw_data = None # Not To be touched

program_index_p1 = 0
def part1(data) -> int:
	data = [int(x) for x in data]

	# This day is the most confusing thing I have ever seen in my life.
	# Incase you don't understand, let me explain this to you in more dept
	# The first number explains the amount of children in the node
	# and the second number explains the amount of metadata

	# Recursive functions which relie on outside variables are sometimes scary for beginners
	def read_tree():
		# First we get the amount of node children and metadata
		global program_index_p1
		nc = data[program_index_p1]
		mc = data[program_index_p1 + 1]
		program_index_p1 += 2

		# Now we create the node
		children = []
		meta_data = []

		# Because the program is dynamically working on 'program_index_p1'
		# calling the function over and over again will cause the 'program_index_p1' to move forward
		# Allowing us to read the amount of children flawlessly
		for _ in range(nc):
			children.append(read_tree())
		
		# Simply read the meta data based on the count and move the program index forward
		meta_data = data[program_index_p1:program_index_p1 + mc]
		program_index_p1 += mc
		
		# Return the node data
		return {
			'children': children,
			'meta_data': meta_data
		}

	tree = read_tree()

	# Now we recursively sum the metadata
	def sum_metadata(node):
		metaSum = 0
		for child in node['children']:
			metaSum += sum_metadata(child)
		metaSum += sum(node['meta_data'])
		return metaSum
	
	return sum_metadata(tree)

program_index_p2 = 0
def part2(data) -> int:
	# The function below is taken from the part above
	data = [int(x) for x in data]
	def read_tree():
		global program_index_p2
		nc = data[program_index_p2]
		mc = data[program_index_p2 + 1]
		program_index_p2 += 2
		children = []
		meta_data = []
		for _ in range(nc):
			children.append(read_tree())
		meta_data = data[program_index_p2:program_index_p2 + mc]
		program_index_p2 += mc
		return {
			'children': children,
			'meta_data': meta_data
		}

	tree = read_tree()
	
	def get_value(node):
		# If the node has no children, we simply return the sum of the metadata
		if len(node['children']) == 0:
			return sum(node['meta_data'])
		else:
			# If the node has children, we loop through the metadata
			value = 0
			for metaData in node['meta_data']:
				# Verifing if the child index is valid, the index starts from 1
				if 0 < metaData <= len(node['children']):
					# Add the value of the referred child to the accumulator
					value += get_value(node['children'][metaData - 1])
			return value
	
	return get_value(tree)