#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Tuple, Dict
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
completed = 1
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
	...