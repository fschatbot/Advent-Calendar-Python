#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = False
raw_data = None # Not To be touched

def part1(data):
	ts, ids = data
	ts = int(ts)

	earliest = float('inf')
	early_id = None
	for id in ids.split(','):
		if id == 'x': continue
		id = int(id)
		d_ts = ((ts // id) + 1) * id
		if d_ts < earliest:
			earliest = d_ts
			early_id = id
	
	return early_id * (earliest - ts)
	

def extendedGCD(a, b):
	if b == 0:
		return a, 1, 0
	
	g, x1, y1 = extendedGCD(b, a % b)

	x = y1
	y = x1 - (a // b) * y1

	return g, x, y

def modInverse(a, m):
	g, x, y = extendedGCD(a, m)
	if g != 1:
		raise ValueError
	
	return (x % m + m) % m
def crt(remainders, moduli):
	prod = 1
	for mod in moduli:
		prod *= mod
	
	ans = 0
	for rem, mod in zip(remainders, moduli):
		pp = prod // mod
		inv = modInverse(pp, mod)
		ans += rem * inv * pp
	return ans % prod

def part2(data):
	# This part can be easily solved using the Chiense Remainder Theorem.
	# Though I wrote the code, I don't know how this theorem or algo works

	rem = []
	mod = []
	_, ids = data
	for i, a in enumerate(ids.split(',')):
		if a == 'x': continue
		mod.append(int(a))
		rem.append(-i % int(a))
	
	return crt(rem, mod)