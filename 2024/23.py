#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):	
	pairings = {}
	for line in data:
		# print(line)
		a, b = line.split('-')
		if a not in pairings:
			pairings[a] = set()
		if b not in pairings:
			pairings[b] = set()
		
		pairings[a].add(b)
		pairings[b].add(a)

	# In order to find a triangle you simply take the intersection of pair[a] and pair[b]
	# This will give you the commons of pair a and pair b which would c. Therefore, a triangle.
	commons = set()
	for line in data:
		a, b = line.split('-')
		common = pairings[a] & pairings[b]
		for c in common:
			if a[0] != 't' and b[0] != 't' and c[0] != 't': continue
			tri = tuple(sorted([a,b,c]))
			commons.add(tri)
	
	return len(commons)

def part2(data):
	pairings = {}
	for line in data:
		# print(line)
		a, b = line.split('-')
		if a not in pairings:
			pairings[a] = set()
		if b not in pairings:
			pairings[b] = set()
		
		pairings[a].add(b)
		pairings[b].add(a)

	# The below is what I implemented on my own. It works but is highly inefficient...
	"""
	def recurse(curr_set):
		if len(curr_set) == 0:
			return 0
		
		return max(recurse(curr_set & pairings[i]) for i in curr_set) + 1
	
	return recurse(set(pairings.keys()))
	"""

	# Bron-Kerbosch algorithm with pivoting...
	def BronKerbosch2(R:set, P:set, X:set):
		if len(P) == 0 and len(X) == 0:
			return R
		
		u = list(P | X)[0]
		max_R = set()
		max_len = 0
		for v in P - pairings[u]:
			r = BronKerbosch2(R | {v}, P & pairings[v], X & pairings[v])
			if len(r) > max_len:
				max_len = len(r)
				max_R = r
			P.remove(v)
			X.add(v)
		
		return max_R
	
	max_R = BronKerbosch2(set(), set(pairings.keys()), set())
	return ','.join(sorted(tuple(max_R)))