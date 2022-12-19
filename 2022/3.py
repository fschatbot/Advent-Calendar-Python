#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = 1
raw_data = None # Not To be touched

def part1(data):
	acc = 0
	for rucksack in data:
		half = len(rucksack) // 2
		comp1, comp2 = rucksack[:half], rucksack[half:]
		commons = set(comp1).intersection(comp2)
		common = list(commons)[0]
		acc += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(common) + 1
	return acc

def part2(data):
	...