#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(data):
	data = data.replace('   ', '\n').split('\n')
	list1 = data[::2]
	list2 = data[1::2]

	return list1, list2

split_data = parse
completed = True
raw_data = None # Not To be touched

def part1(data):
	list1, list2 = data
	cum = 0
	for l1, l2 in zip(sorted(list1), sorted(list2)):
		cum += abs(int(l1) - int(l2))
	
	return cum
	

def part2(data):
	list1, list2 = data

	hashmap = {} # Quick hashmap to store the frequency for later use
	for elem in list2:
		hashmap[elem] = hashmap.get(elem, 0) + 1
	
	simScore = 0
	for elem in list1:
		simScore += int(elem) * hashmap.get(elem, 0)
	
	return simScore