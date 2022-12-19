#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = True
completed = True
raw_data = None # Not To be touched

def part1(data):
	final_score = 0

	translation = {
		'A': 'rock',
		'B': 'paper',
		'C': 'scissor',
		'X': 'rock',
		'Y': 'paper',
		'Z': 'scissor'
	}

	scoring = { # Score for each choice
		'rock': 1,
		'paper': 2,
		'scissor': 3
	}

	winCondition = { # lose against win --> loose: win
		'rock': 'paper',
		'paper': 'scissor',
		'scissor': 'rock'
	}

	for step in data:
		opponent, you = step.split(' ')
		opponent, you = translation[opponent], translation[you] # Convert ABCXYZ into rock paper scissor
		outcome = 0

		if opponent == you:
			outcome = 3
		elif winCondition[opponent] == you:
			outcome = 6
		
		final_score += outcome + scoring[you]
	
	return final_score

def part2(data):
	final_score = 0

	translation = {
		'A': 'rock',
		'B': 'paper',
		'C': 'scissor',
	}

	scoring = { # Score for each choice
		'rock': 1,
		'paper': 2,
		'scissor': 3
	}

	winCondition = { # lose against win --> loose: win
		'rock': 'paper',
		'paper': 'scissor',
		'scissor': 'rock'
	}

	for step in data: # loop through the guide
		opponent, you = step.split(' ')
		opponent = translation[opponent]
		choice = None
		outcome = 0

		if you == 'X':
			outcome = 0
			choice = list(winCondition.keys())[list(winCondition.values()).index(opponent)]
		elif you == 'Y':
			choice = opponent
			outcome = 3
		elif you == 'Z':
			choice = winCondition[opponent]
			outcome = 6
		
		final_score += scoring[choice] + outcome
	
	return final_score