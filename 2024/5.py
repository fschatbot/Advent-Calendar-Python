#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(data):
	rules, updates = data.split('\n\n')
	rules = [x.split('|') for x in rules.split('\n')]
	updates = [x.split(',') for x in updates.split('\n')]

	return rules, updates

split_data = parse
completed = True
raw_data = None # Not To be touched


def part1(data):
	rules, updates = data
	def valid(rules, update):
		return not any(update.index(b) < update.index(a) for a, b in rules if a in update and b in update)
	return sum(int(update[len(update) // 2]) for update in updates if valid(rules, update))

def part2(data):
	rules, updates = data

	total = 0
	for update in updates:
		edited = False
		editing = True

		while editing:
			for ra, rb in rules:
				if ra not in update or rb not in update: continue
				rai = update.index(ra)
				rbi = update.index(rb)
				if rai < rbi: continue # Rule passed
				edited = True

				update.insert(rbi, update.pop(rai)) # Add them before the rbi to satisfy the condition
				break
			else:
				editing = False

		
		if not edited: continue
		total += int(update[len(update) // 2])

	
	return total

