#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

class Cardv1:
	strengthOrder = '23456789TJQKA'
	def __init__(self, hand:str, bid:int) -> None:
		self._hand = hand
		self.bid = int(bid)

		self.Handtype = 0
		unique = {card: hand.count(card) for card in hand}
		uniqueLen = len(unique)
		if uniqueLen == 1:
			self.Handtype = 6 # Five of a kind
		elif any(c == 4 for c in unique.values()):
			self.Handtype = 5 # Four of a kind
		elif uniqueLen == 2 and any(c == 3 for c in unique.values()):
			self.Handtype = 4 # Full house
		elif any(c == 3 for c in unique.values()):
			self.Handtype = 3 # Three of a kind
		elif sum(1 for c in unique.values() if c == 2) == 2:
			self.Handtype = 2 # Two pair
		elif sum(1 for c in unique.values() if c == 2) == 1:
			self.Handtype = 1 # One pair
		else:
			self.Handtype = 0 # High card

		self.Handstrength = []
		for card in self._hand:
			self.Handstrength.append(Cardv1.strengthOrder.index(card))

def part1(data):
	cards = []
	for line in data:
		cards.append(Cardv1(*line.split(' ')))
	
	cards.sort(key=lambda c: (c.Handtype, *c.Handstrength))

	acc = 0
	for rank, card in enumerate(cards, start=1):
		acc += rank * card.bid
	return acc

class Cardv2:
	strengthOrder = 'J23456789TQKA'
	def __init__(self, hand:str, bid:int) -> None:
		self._hand = hand
		self.bid = int(bid)

		self.Handtype = 0
		# Just pick the most occurring card and use that for J
		highestOccur = max([c for c in (hand.replace('J', '') or 'J')], key=lambda c: hand.count(c))
		handv2 = ''.join(highestOccur if c == 'J' else c for c in hand)
		
		unique = {card: handv2.count(card) for card in handv2}
		uniqueLen = len(unique)
		if uniqueLen == 1:
			self.Handtype = 6 # Five of a kind
		elif any(c == 4 for c in unique.values()):
			self.Handtype = 5 # Four of a kind
		elif uniqueLen == 2 and any(c == 3 for c in unique.values()):
			self.Handtype = 4 # Full house
		elif any(c == 3 for c in unique.values()):
			self.Handtype = 3 # Three of a kind
		elif sum(1 for c in unique.values() if c == 2) == 2:
			self.Handtype = 2 # Two pair
		elif sum(1 for c in unique.values() if c == 2) == 1:
			self.Handtype = 1 # One pair
		else:
			self.Handtype = 0 # High card

		self.Handstrength = []
		for card in self._hand:
			self.Handstrength.append(Cardv2.strengthOrder.index(card))

def part2(data):
	cards = []
	for line in data:
		cards.append(Cardv2(*line.split(' ')))
	
	cards.sort(key=lambda c: (c.Handtype, c.Handstrength))

	acc = 0
	for rank, card in enumerate(cards, start=1):
		acc += rank * card.bid
	return acc