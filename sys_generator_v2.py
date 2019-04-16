'''
Last Edited: 13 Apr 2019 11:10 PM

Edited by HX: Ongoing


In this script, we are going to generate the permutations of the given blocks within the griven 
grid size. To save memory space and computation time, we are not going to record all the possible 
permutations, but rather, systematically check each permutation, and break out from the loop when 
a solution is found. Futher, for the positon of the first block, we will only consider the blocks 
in the direction of laser. 

'''



import random
import copy
from random import sample

# !!! Ensure the laser module is computing the same game level
import laser
from laser import intcp
from laser import Laser


#################################################
#The following code performs input manipulation #
#################################################



fptr = open('yarn_5.bff', 'r').read()
all_lines = fptr.split('\n')
raw_data = []

# Split raw data by line into a list
for line in all_lines:
	if '#' not in line and line != '':
		raw_data.append(line)
#print(raw_data)

# Split list into sublists to facilitate extraction of data into grid, blocks, laser, and destination points
setup = fptr.split('\n')[9:]
#print(setup)


#################################################
#The following code Generating the game grid    #
#################################################


grid_start = raw_data.index('GRID START')
grid_stop = raw_data.index('GRID STOP')

grid_raw = raw_data[grid_start+1:grid_stop]

grid = []

for i in grid_raw:
	trial_list = []
	x = ''.join(i.split())
	for letter in x:
		trial_list.append(letter)
	grid.append(trial_list)

for line in grid_raw:
	if line in raw_data:
		raw_data.remove(line)

# print grid


blocks = {}

for line in raw_data:
	if line.startswith('A') == True or line.startswith('B') == True or line.startswith('C') == True:
		line = line.split()
		key = line[0]
		blocks[key] = int(line[1])

if 'A' not in blocks.keys():
	blocks.update({'A':0})

if 'B' not in blocks.keys():
	blocks.update({'B':0})

if 'C' not in blocks.keys():
	blocks.update({'C':0})

## First we will flatten the array into a 2D list for the sake of convenience and binning.

net_grid = [i for j in grid for i in j]

#print net_grid


## Replacing the string vacancies to integers

#for n,i in enumerate(net_grid):
	#if i == 'o':
		#net_grid[n] = 0

#################################################
#The following code Generating the game path    #
#################################################


# Obtaining Laser path to get a list of likely positions for first block

# Method 1. Use laser positon and direction only
# 			Get the length from laser to the edge of grid at laser direction, 
#			generate all the position in laser path 
#			check if the block position (laser path position (x+/-1, y+/-1)) is in net_grid,
#			if so, add to list 


# Method 2. use laser path already calculated in laser file
#			Note: ameya needs to correct the trajectory() such that 
#			1. the codes reads in raw input of block/laser position
#			2. the code responses to different block properly 
#			?? This might increase computing need ??

# The following code generates all the allowed block coordinates in a list 
all_block_pos = []
for i in range(len(grid)):
	for j in range(len(grid[0])):
		all_block_pos.append((2*j+1, 2*i + 1))

#print all_block_pos

print net_grid

def Sys_Generator(net_grid, blocks, steps):

	# Applying Method 2:

	neighbor_direction = [(0 , 1), (0 , -1), (1, 0), (-1, 0)]
	likely_pos_1stblock = []

	for i in intcp:
		for j in neighbor_direction:
			each_pos_x = i[0] + j[0]
			each_pos_y = i[1] + j[1]
			each_pos = (each_pos_x, each_pos_y)

			if each_pos not in likely_pos_1stblock:
				likely_pos_1stblock.append(each_pos)

				if each_pos not in all_block_pos: 
					likely_pos_1stblock.pop()


	nA = blocks['A']
	nB = blocks['B']
	nC = blocks['C']
	ensemble = []

	n_total = nA + nB + nC

	count = 0

	# likely_pos_1stblock is a list of "allowed" positions for the 1st block to be placed on grid
	#print likely_pos_1stblock


	for i in range(0,steps):

		nA = blocks['A']
		nB = blocks['B']
		nC = blocks['C']
		n_total = nA + nB + nC

	
		new_grid = []
		block_index_list = []

		rand_1st_block = random.sample(likely_pos_1stblock, 1)[0]
		#print rand_1st_block

		block_index = all_block_pos.index(rand_1st_block)


		#block_index_list is a list of indexes of random block positions

		block_index_list.append(block_index)

		rand_i = random.sample(range(0,len(net_grid)), n_total - 1)
		if block_index not in rand_i:
			block_index_list.append(rand_i)


			for j in range(len(net_grid)):
				if net_grid[j] == 'o':
					if j in block_index_list:
						if nA > 0:
							new_grid.append('A')
							nA = nA - 1
						if nA == 0 and nB >0:
							new_grid.append('B')
							nB = nB - 1

						elif nA == 0 and nB == 0 and nC >0:
							new_grid.append('C')
							nC = nC - 1


					else:
						new_grid.append('o')

				else:
					new_grid.append(net_grid[j])

				# print new_grid

			ensemble.append(new_grid)

	return ensemble


	




# #################################################
# HX Note to self:
# now the coordinates to the 1st block probable position is identified, it needs to be converted to actual sequence
# You have mapped all the possible positions of blocks, simplely numerate the net_grid list, correlate it to the sequence list
# and do random seletion of position for 1st block, followed by putting it back to 
# #################################################


if __name__ == "__main__":

	a = Sys_Generator(net_grid, blocks, 10)
	print len(a)



	# ans = MC_Generator(net_grid, blocks, 10)

	# ## To get back the grid in the game format from the code

	# for i in ans:
	# 	A = [i[x:x+4] for x in range(0,len(i),4)]
	# 	print(A)


