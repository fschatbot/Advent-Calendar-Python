#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = '\n\n'
completed = True
raw_data = None # Not To be touched

def part1(data):
	all_cals = []
	for elf_rations in data:
		elf_cal = sum(int(food) for food in elf_rations.split('\n'))
		all_cals.append(elf_cal)
	return max(all_cals)

def part2(data):
	all_cals = []
	for elf_rations in data:
		elf_cal = sum(int(food) for food in elf_rations.split('\n'))
		all_cals.append(elf_cal)
	return sum(sorted(all_cals)[-3:])