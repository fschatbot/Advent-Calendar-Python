#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil

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
completed = True
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

	def createFuel(fuelAmount, initialReserve):
		"""Calculates the amount of ores required and leftOvers"""
		reserve = initialReserve
		ore_amount = 0

		new_orders = {'FUEL': fuelAmount}
		last_orders = {}
		# Expand the new chemicals until all that is left is ORE
		while new_orders:
			last_orders = new_orders
			new_orders = {}

			# Go through each order
			for chemical, amount in last_orders.items():
				if chemical == 'ORE':
					ore_amount += amount
				elif reserve.get(chemical, 0) >= amount:
					reserve[chemical] -= amount
				else:
					# Calculate the amount of batches we need to make
					need = amount - reserve.get(chemical, 0) # The order - the reserve
					batch = ceil(need / data[chemical]['quantity']) # need / quantity per batch
					# Make the batches
					for reactant in data[chemical]['reactants']:
						new_orders[reactant[1]] = new_orders.get(reactant[1], 0) + reactant[0] * batch # Add child reactants * batch
					# Store the leftovers
					reserve[chemical] = batch * data[chemical]['quantity'] - need # made - need
		return ore_amount, reserve
	
	# Keep estimating the amount of fuel we can make with remain ores
	# 1. estimate the amount of fuel we can make with the ores
	# 2. Caclulate the actual amount of ores used
	# 3. Delete the used ores from the reserve
	# 4. Repeat till the estimate is 0

	oresUsed = 0
	reserve = {}
	fuelMade = 0
	oneFuelEstimate,_ = createFuel(1, reserve)
	while oresUsed < INITIAL_ORE_DEPOSIT:
		estimate = (INITIAL_ORE_DEPOSIT - oresUsed) // oneFuelEstimate
		if estimate == 0: return int(fuelMade)
		ores, reserve = createFuel(int(estimate), reserve.copy())
		fuelMade += estimate
		oresUsed += ores