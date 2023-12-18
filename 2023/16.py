#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

split_data = True
completed = True
raw_data = None # Not To be touched


class Subscriptable:
	# https://stackoverflow.com/a/68982326
    def __class_getitem__(cls, item):
        return cls._get_child_dict()[item]

    @classmethod
    def _get_child_dict(cls):
        return {k: v for k, v in cls.__dict__.items() if not k.startswith('_')}

class DIRECTION(Subscriptable):
	UP    = (0, -1)
	DOWN  = (0, +1)
	LEFT  = (-1, 0)
	RIGHT = (+1, 0)

class Beam:
	def __init__(self, xy, dir):
		self.x, self.y = xy
		self.dirN = dir
		self.dir = DIRECTION[dir]
		self.hash = f"{self.x},{self.y}|{self.dirN[0]}"
	
	def next(self, map):
		lx, ly = len(map[0]), len(map)
		if not (0 <= self.x < lx and 0 <= self.y < ly): return
		char = map[self.y][self.x]

		rightSlatMirr = { # /
			'DOWN': 'LEFT',
			'LEFT': 'DOWN',
			'UP': 'RIGHT',
			'RIGHT': 'UP'
		}
		leftSlatMirr = { # \
			'DOWN': 'RIGHT',
			'RIGHT': 'DOWN',
			'LEFT': 'UP',
			'UP': 'LEFT',
		}

		if char == '-' and self.dirN in ('RIGHT', 'LEFT'):
			yield Beam((self.x + self.dir[0], self.y), self.dirN)
		elif char == '|' and self.dirN in ('UP', 'DOWN'):
			yield Beam((self.x, self.y + self.dir[1]), self.dirN)
		elif char == '-' and self.dirN in ('UP', 'DOWN'):
			yield Beam((self.x-1, self.y), 'LEFT')
			yield Beam((self.x+1, self.y), 'RIGHT')
		elif char == '|' and self.dirN in ('LEFT', 'RIGHT'):
			yield Beam((self.x, self.y-1), 'UP')
			yield Beam((self.x, self.y+1), 'DOWN')
		elif char == '/':
			new_dir = rightSlatMirr[self.dirN]
			nx, ny = self.x + DIRECTION[new_dir][0], self.y + DIRECTION[new_dir][1]
			yield Beam((nx, ny), new_dir)
		elif char == '\\':
			new_dir = leftSlatMirr[self.dirN]
			nx, ny = self.x + DIRECTION[new_dir][0], self.y + DIRECTION[new_dir][1]
			yield Beam((nx, ny), new_dir)
		elif char == '.':
			yield Beam((self.x + self.dir[0], self.y + self.dir[1]), self.dirN)			
		else:
			print('How did we get here?')
			print(char, nx, ny)
	
	def __str__(self) -> str:
		return f"<Beam dir=\"{self.dirN}\" xy={self.x},{self.y} />"
	def __repr__(self) -> str:
		return f"<Beam dir=\"{self.dirN}\" xy={self.x},{self.y} />"

def part1(data:List[str]):
	seen = set()
	uniqueSeen = set()
	queue = [Beam((0, 0), 'RIGHT')]
	lx, ly = len(data[0]), len(data)

	while queue:
		beam = queue.pop(0)
		seen.add(beam.hash)
		uniqueSeen.add((beam.x, beam.y))
		for new_beam in beam.next(data):
			if new_beam.hash in seen: continue
			if not (0 <= new_beam.x < lx and 0 <= new_beam.y < ly): continue
			queue.append(new_beam)
	
	return len(uniqueSeen)

def part2(data:List[str]):
	lx, ly = len(data[0]), len(data)
	best = 0
	config = []

	for x in range(lx):
		config.append(Beam((x, 0), 'DOWN'))
		config.append(Beam((x, ly-1), 'UP'))
	for y in range(ly):
		config.append(Beam((0, y), 'RIGHT'))
		config.append(Beam((lx-1, y), 'LEFT'))

	while config:
		seen = set()
		uniqueSeen = set()
		queue = [config.pop(0)]

		while queue:
			beam = queue.pop(0)
			seen.add(beam.hash)
			uniqueSeen.add((beam.x, beam.y))
			for new_beam in beam.next(data):
				if new_beam.hash in seen: continue
				if not (0 <= new_beam.x < lx and 0 <= new_beam.y < ly): continue
				queue.append(new_beam)

		best = max(len(uniqueSeen), best)
	
	return best