#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

# We have added dummy rings and armor so it can simiulate choosing "nothing"
shop = {
	"weapons": [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)],
	"armor": [(0, 0), (13, 1), (31, 2), (53, 3), (75, 4), (102, 5)],
	"rings": [(0,0,0), (0,0,0), (25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3)]
}

def part1(data):
	enemy_health, enemy_damage, enemy_armor = (int(line.split(":")[1]) for line in data)

	best_cost = float('inf')

	for wc, wd in shop['weapons']:
		for ac, ad in shop['armor']:
			for i, rls in enumerate(shop['rings']):
				for rrs in shop['rings'][i+1:]:
					cost = wc + ac + rls[0] + rrs[0]
					damage = wd + rls[1] + rrs[1]
					armor = ad + rls[2] + rrs[2]

					# Now we need our effective damage to be higher than the enemies effective damage
					# For the math to be correct we would need +1 on both sides (because ceil not floor). That cancels out so not required.
					if enemy_health // max(damage - enemy_armor, 1) > 100 // max(enemy_damage - armor, 1): continue

					best_cost = min(best_cost, cost)
	
	return best_cost



def part2(data):
	enemy_health, enemy_damage, enemy_armor = (int(line.split(":")[1]) for line in data)

	most_cost = 0

	for wc, wd in shop['weapons']:
		for ac, ad in shop['armor']:
			for i, rls in enumerate(shop['rings']):
				for rrs in shop['rings'][i+1:]:
					cost = wc + ac + rls[0] + rrs[0]
					damage = wd + rls[1] + rrs[1]
					armor = ad + rls[2] + rrs[2]

					# Now we need our effective rounds to be higher than the enemy
					# For the math to be correct we would need +1 on both sides (because ceil not floor). That cancels out so not required.
					if enemy_health // max(damage - enemy_armor, 1) <= 100 // max(enemy_damage - armor, 1): continue

					most_cost = max(most_cost, cost)
	
	return most_cost