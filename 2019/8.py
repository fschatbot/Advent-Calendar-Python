#!/usr/bin/env python
# -*- coding: utf-8 -*-

split_data = False
completed = True
raw_data = None # Not To be touched

def part1(data):
	imagePixels = 25 * 6 # The amount of pixels in each layer
	layers = [data[n:n+imagePixels] for n in range(0, len(data), imagePixels)] # Splits the data into flat layers
	# Finding the layer with the least `0` digit
	layer = min(layers, key= lambda layer: layer.count('0'))
	return layer.count('1') * layer.count('2')

def part2(data):
	imagePixels = 25 * 6 # The amount of pixels in each layer
	layers = [data[n:n+imagePixels] for n in range(0, len(data), imagePixels)] # Splits the data into flat layers
	final_layer = ''

	# Loop through each pixel and then each layer, if trnasparent then skip it otherwise add it to the final_layer
	for i in range(imagePixels):
		for layer in layers:
			if layer[i] == '2': continue
			final_layer += layer[i]
			break
		else:
			final_layer += '2' # All the layers were transparent
	final_layer = final_layer.replace('1', '\u2588').replace('0', ' ') # Special Characters to help see
	layer_split = [final_layer[n:n+25] for n in range(0, len(final_layer), 25)]
	print('\n'.join(layer_split))