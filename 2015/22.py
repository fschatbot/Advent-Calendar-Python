#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

from heapq import heappop, heappush

def part1(data):
	enemy_health, enemy_damage = (int(line.split(":")[1]) for line in data)
	# We will compensate the player for letting the boss get a free turn
	states = [(0, enemy_health, 50 + enemy_damage, 500, 0, 0, 0)]
	# state = (used mana, enemy health, current health, current mana, shield timer, poison timer, recharge timer)
	while states:
		um, eh, ch, cm, st, pt, rt = heappop(states)
		if eh <= 0:
			return um # Got a enemy death
		# BOSS's TURN

		# Simulate the timers...
		if st > 0:
			st -= 1
			ch -= max(enemy_damage - 7, 1)
		else:
			ch -= enemy_damage
		if ch <= 0:
			continue # Player died
		if pt > 0:
			pt -= 1
			eh -= 3
		if rt > 0:
			rt -= 1
			cm += 101
		
		# Player turn's timer
		if st > 0:
			st -= 1
		if pt > 0:
			pt -= 1
			eh -= 3
		if rt > 0:
			rt -= 1
			cm += 101
		
		for attack, cost in [("MM", 53), ("D", 73), ("S", 113), ("P", 173), ("R", 229)]:
			if cost > cm: continue
			if attack == "MM":
				heappush(states, (um+cost,eh-4,ch,cm-cost,st,pt,rt))
			elif attack == "D":
				heappush(states, (um+cost,eh-2,ch+2,cm-cost,st,pt,rt))
			elif attack == "S" and st == 0:
				heappush(states, (um+cost,eh,ch,cm-cost,6,pt,rt))
			elif attack == "P" and pt == 0:
				heappush(states, (um+cost,eh,ch,cm-cost,st,6,rt))
			elif attack == "R" and rt == 0:
				heappush(states, (um+cost,eh,ch,cm-cost,st,pt,5))

def part2(data):
	enemy_health, enemy_damage = (int(line.split(":")[1]) for line in data)
	# We will compensate the player for letting the boss get a free turn
	states = [(0, enemy_health, 50 + enemy_damage, 500, 0, 0, 0)]
	# state = (used mana, enemy health, current health, current mana, shield timer, poison timer, recharge timer)
	while states:
		um, eh, ch, cm, st, pt, rt = heappop(states)
		if eh <= 0:
			return um # Got a enemy death
		# BOSS's TURN

		# Simulate the timers...
		if st > 0:
			st -= 1
			ch -= max(enemy_damage - 7, 1)
		else:
			ch -= enemy_damage
			
		if ch <= 0:
			continue # Player died
		
		if pt > 0:
			pt -= 1
			eh -= 3
		if rt > 0:
			rt -= 1
			cm += 101
		
		# Player turn's timer
		ch -= 1
		if ch <= 0:
			continue
		
		if st > 0:
			st -= 1
		if pt > 0:
			pt -= 1
			eh -= 3
		if rt > 0:
			rt -= 1
			cm += 101
		
		for attack, cost in [("MM", 53), ("D", 73), ("S", 113), ("P", 173), ("R", 229)]:
			if cost > cm: continue
			if attack == "MM":
				heappush(states, (um+cost,eh-4,ch,cm-cost,st,pt,rt))
			elif attack == "D":
				heappush(states, (um+cost,eh-2,ch+2,cm-cost,st,pt,rt))
			elif attack == "S" and st == 0:
				heappush(states, (um+cost,eh,ch,cm-cost,6,pt,rt))
			elif attack == "P" and pt == 0:
				heappush(states, (um+cost,eh,ch,cm-cost,st,6,rt))
			elif attack == "R" and rt == 0:
				heappush(states, (um+cost,eh,ch,cm-cost,st,pt,5))