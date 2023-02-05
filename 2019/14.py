#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil
from collections import Counter

def process_data(data):
	map = {}
	for line in data.split('\n'):
		reactants, product = line.split('=>')
		# Spliting the reactants: [(2, 'A'), (3, 'B'), ...]
		reactants = [reactant.strip().split(' ') for reactant in reactants.split(',')]
		reactants = [(int(reactant[0]), reactant[1]) for reactant in reactants]
		# Spliting the product: (5, 'AB')
		quantity, chemical = product.strip().split(' ')
		quantity = int(quantity)
		map[chemical] = {"quantity": quantity, "reactants": reactants}
	return map


split_data = process_data
completed = 1
raw_data = None # Not To be touched

def part1(data):
	reserve = {} # stores the chemicals which are left over
	ore_counter = 0

	def createChemical(chemical):
		nonlocal ore_counter
		for reactant in data[chemical]['reactants']:
			if reactant[1] == 'ORE':
				ore_counter += reactant[0]
			else:
				# Add the chemical to the reserve
				if reactant[1] not in reserve: reserve[reactant[1]] = 0
				# Keep creating the chemical till we have enough
				while reactant[0] > reserve[reactant[1]]:
					reserve[reactant[1]] += createChemical(reactant[1])
				# The amount we created minus the amount we used for this reaction
				reserve[reactant[1]] -= reactant[0]
		
		return data[chemical]['quantity']

	createChemical('FUEL')
	return ore_counter

def part2(data):
	INITIAL_ORE_DEPOSIT = 1e12 # 1 trillion

	def createFuel(fuelAmount):
		"""Calculates the amount of ores required and leftOvers"""
		reserve = {}
		ore_amount = 0

		new_chemicals = {'FUEL': fuelAmount}
		last_chemicals = {}
		# Expand the new chemicals until all that is left is ORE
		while any(chemical != 'ORE' for chemical in new_chemicals):
			last_chemicals = new_chemicals
			new_chemicals = {}
			for chemical in last_chemicals:
				if chemical == 'ORE':
					ore_amount += last_chemicals[chemical]
					continue
					
				need = last_chemicals[chemical] - reserve.get(chemical, 0)
				made  = data[chemical]['quantity'] * ceil(need / data[chemical]['quantity'])
				reserve[chemical] = made - need

				for _ in range(made):
					for reactant in data[chemical]['reactants']:
						new_chemicals[reactant[1]] = new_chemicals.get(reactant[1], 0) + reactant[0]
				# print(need, made)
				# exit()

				# for reactant in data[chemical]['reactants']:
				# 	new_chemicals[reactant[1]] = new_chemicals.get(reactant[1], 0) + reactant[0] * ceil(need / data[chemical]['quantity'])
			# print(new_chemicals)
			

		return ore_amount, reserve
	
	# estimate = INITIAL_ORE_DEPOSIT // createFuel(1)[0]
	# ores, reserve = createFuel(int(estimate))
	ores, reserve = createFuel(1)
	print(ores, reserve)
	return
		


	reserve = {'ORE': INITIAL_ORE_DEPOSIT} # stores the chemicals which are left over

	def createChemical(chemical):
		if chemical == 'ORE': raise Exception("We can't create ORE silly! 🤭")
		for reactant in data[chemical]['reactants']:			
			if reactant[1] not in reserve: reserve[reactant[1]] = 0 # Add the chemical to the reserve
			
			# Keep creating the chemical till we have enough
			while reactant[0] > reserve[reactant[1]]:
				reserve[reactant[1]] += createChemical(reactant[1])
			
			# The amount we created minus the amount we used for this reaction
			reserve[reactant[1]] -= reactant[0]
		
		return data[chemical]['quantity'] # return the quantity we have made
	
	# The way we are achive the number simply through finding a sitaution where the reserve is empty again
	# This will leave us in the exact same position as start expect we would know the extact number of FUEL
	# we can make with no leftovers. From there its simple maths!!

	FuelCounter = 0
	memory = []
	# Generating fuel until we have no leftovers
	while any(reserve[chemical] != 0 for chemical in reserve if chemical != 'ORE') or FuelCounter == 0:
		FuelCounter += createChemical('FUEL')
		if {chemical: int(reserve[chemical]) for chemical in reserve if chemical != 'ORE'} in memory:
			print("!!! RED ALERT")
		memory.append({chemical: int(reserve[chemical]) for chemical in reserve if chemical != 'ORE'})
	
	from pathlib import Path
	import json
	Path("2019/temp2.json").write_text(json.dumps(memory))
	
	# The amount of ores that can be converted into fuel with 0 leftovers
	goldenOreNumber = INITIAL_ORE_DEPOSIT - reserve['ORE']
	# Simple maths to skip most of the work
	FuelCounter  = (INITIAL_ORE_DEPOSIT // goldenOreNumber) * FuelCounter
	reserve['ORE'] = INITIAL_ORE_DEPOSIT - (INITIAL_ORE_DEPOSIT // goldenOreNumber) * goldenOreNumber

	# Generating whatever we can from the left over ores
	while True:
		try: FuelCounter += createChemical('FUEL')
		except: return FuelCounter

