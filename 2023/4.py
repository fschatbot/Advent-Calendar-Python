#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data) -> int:
	acc = 0
	for card in data:
		card = re.sub(r'\s+', ' ', card)
		winningNumbers, scratchedNumbers = card.split(': ')[1].split(' | ')
		winningNumbers, scratchedNumbers = winningNumbers.split(' '), scratchedNumbers.split(' ')
		matched = sum(1 for number in scratchedNumbers if number in winningNumbers)
		acc += 2 ** (matched-1) if matched > 0 else 0
	return acc


def part2(data):
	cards = [] # Includes the number of matches at n-1 index: {'matches': int, 'count': int | default: 1}
	for card in data:
		card = re.sub(r'\s+', ' ', card)
		winningNumbers, scratchedNumbers = card.split(': ')[1].split(' | ')
		winningNumbers, scratchedNumbers = winningNumbers.split(' '), scratchedNumbers.split(' ')
		matched = sum(1 for number in scratchedNumbers if number in winningNumbers)
		cards.append({'wins': matched, 'count': 1})
	
	# Now we do the weird behaviour of multiplication down the line
	for id, card in enumerate(cards):
		for updateId in range(id+1, min(id+card['wins']+1, len(cards))):
			cards[updateId]['count'] += card['count']
	
	# Counting the number of total cards in the end
	return sum(card['count'] for card in cards)