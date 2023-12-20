#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Tuple, Dict
from copy import deepcopy
import re

def parse(data:str) -> Tuple[Dict[str, List], List[Dict]]:
	workflows, parts = data.split('\n\n')
	workflow = {}
	
	ruleRegex = re.compile(r'(\w+)(<|>)(\d+)')
	for line in workflows.split('\n'):
		name, rules = line[:-1].split('{')
		rules = [rule.split(':') for rule in rules.split(',')]
		workflowMap = []
		for rule in rules:
			if len(rule) == 2:
				_, key, operator, value, _ = ruleRegex.split(rule[0])
				workflowMap.append({"key": key, "operator": operator, "value": int(value), "action": rule[1], 'isLast': False})
			elif len(rule) == 1:
				workflowMap.append({"action": rule[0], 'isLast': True})
		
		workflow[name] = workflowMap
	
	partList = []
	digitRegex = re.compile(r'\d+')
	for part in parts.split('\n'):
		x, m, a, s = digitRegex.findall(part)
		partList.append({"x": int(x), "m": int(m), "a": int(a), "s": int(s)})
	
	return workflow, partList

split_data = parse
completed = True
raw_data = None # Not To be touched

def part1(data:Tuple[Dict[str, List], List[Dict]]):
	workflow, partList = data

	def isAccepted(part, workflowName):
		if workflowName == 'A': return True
		elif workflowName == 'R': return False

		if workflowName not in workflow: print('How did we get here?', part, workflowName) # Debug

		rules = workflow[workflowName]
		for rule in rules:
			if rule['isLast']: return isAccepted(part, rule['action'])

			if rule['operator'] == '>' and part[rule['key']] > rule['value']:
				return isAccepted(part, rule['action'])
			elif rule['operator'] == '<' and part[rule['key']] < rule['value']:
				return isAccepted(part, rule['action'])
	
	acc = 0
	for part in partList:
		if not isAccepted(part, 'in'): continue
		acc += sum(part.values())
	
	return acc

def part2(data:List[str]):
	workflow = data[0] # We don't need the second thing!
	
	queue = [{'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000], 'workflow': 'in'}] # I am not writting the entire obj （︶^︶）
	accepted = 0

	while queue:
		item = queue.pop(0)
		if item['workflow'] == 'A':
			# numpy.prod doesn't work for odd reasons!
			processed = [item[k][1] - item[k][0] + 1 for k in 'xmas']
			accepted += processed[0] * processed[1] * processed[2] * processed[3]
			continue
		elif item['workflow'] == 'R':
			continue
		rules = workflow[item['workflow']]

		for rule in rules:
			# There are three possibility!
			# 1. Its > and entire thing is above. In which case, break and append the entire thing back with the different workflow
			# 2. Its < and entire thing is below. In which case, break and append the entire thing back with the different workflow
			# 3. The value is in the middle of the min and max. In which case, we edit the item to that what didn't match and continue
			# 3.a We take the part which matched and add to the queue
			# 3.b We edit the item currently under inspection to the condition that would fail the rule

			if rule['isLast']:
				queue.append({**item, 'workflow': rule['action']}) # Last rule
				continue

			minN, maxN = item[rule['key']]
			if rule['operator'] == '>' and minN > rule['value']:
				queue.append({**item, 'workflow': rule['action']}) # The entire item works
				break
			elif rule['operator'] == '<' and maxN < rule['value']:
				queue.append({**item, 'workflow': rule['action']}) # The entire item works
				break
			elif rule['operator'] == '>' and maxN > rule['value'] and minN <= rule['value']:  # Some of the item works
				newItem = deepcopy(item)
				newItem['workflow'] = rule['action']
				newItem[rule['key']][0] = rule['value'] + 1
				queue.append(newItem)
				item[rule['key']][1] = rule['value']
			elif rule['operator'] == '<' and minN < rule['value'] and maxN >= rule['value']:  # The entire item works
				newItem = deepcopy(item)
				newItem['workflow'] = rule['action']
				newItem[rule['key']][1] = rule['value'] - 1
				queue.append(newItem)
				item[rule['key']][0] = rule['value']

	return accepted