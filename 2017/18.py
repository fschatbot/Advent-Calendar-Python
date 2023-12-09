#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

split_data = True
completed = True
raw_data = None # Not To be touched


def part1(data:List[str]):
	playedSound = None
	register = {}
	def parse(val):
		return register[val] if len(val) == 1 and not val.isdigit() else int(val)
	
	i = 0
	while i < len(data):
		ins, vals = data[i].split(' ', 1)
		vals = vals.split(' ')
		if ins == 'snd':
			playedSound = parse(vals[0])
		elif ins == 'set':
			x, y = vals
			register[x] = parse(y)
		elif ins == 'add':
			x, y = vals
			register[x] = register.get(x, 0) + parse(y)
		elif ins == 'mul':
			x, y = vals
			register[x] = register.get(x, 0) * parse(y)
		elif ins == 'mod':
			x, y = vals
			register[x] = register.get(x, 0) % parse(y)
		elif ins == 'rcv':
			if parse(vals[0]) != 0:
				return playedSound
		
		if ins == 'jgz':
			x, y = vals
			if parse(x) > 0:
				i += parse(y)
			else:
				i += 1
		else:
			i += 1

class Program:
	def __init__(self, register:dict, ins:List[str]):
		self.register = register
		self.ins = ins
		self.sending = []
		self.recived = []
		self.i = 0
		self.waiting = False
		self.terminated = False
	
	def parse(self, val):
		return self.register[val] if len(val) == 1 and not val.isdigit() else int(val)
	
	def run(self):
		self.waiting = False
		while self.i < len(self.ins):
			ins, vals = self.ins[self.i].split(' ', 1)
			vals = vals.split(' ')
			if ins == 'snd':
				self.sending.append(self.parse(vals[0])) # Sending value over
			elif ins == 'set':
				x, y = vals
				self.register[x] = self.parse(y)
			elif ins == 'add':
				x, y = vals
				self.register[x] = self.register.get(x, 0) + self.parse(y)
			elif ins == 'mul':
				x, y = vals
				self.register[x] = self.register.get(x, 0) * self.parse(y)
			elif ins == 'mod':
				x, y = vals
				self.register[x] = self.register.get(x, 0) % self.parse(y)
			elif ins == 'rcv':
				if len(self.recived) == 0:
					self.waiting = True
					return
				self.register[vals[0]] = self.recived.pop(0)
				

			if ins == 'jgz':
				x, y = vals
				if self.parse(x) > 0:
					self.i += self.parse(y)
				else:
					self.i += 1
			else:
				self.i += 1
		self.terminated = True


def part2(data:List[str]):
	counter = 0
	program1 = Program({'p': 0}, data)
	program2 = Program({'p': 1}, data)
	while not all(pro.terminated or (pro.waiting and len(pro.recived) == 0) for pro in [program1, program2]):
		program1.run()
		program2.run()

		counter += len(program2.sending)
		
		program2.recived = program1.sending.copy()
		program1.recived = program2.sending.copy()
		program1.sending = []
		program2.sending = []
	
	return counter