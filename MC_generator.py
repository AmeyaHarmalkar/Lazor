'''
Last Edited: 13 Apr 2019 11:10 PM

Edited by HX: Ongoing until 1 AM 14 Apr 2019, committed every 20 minutes


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


#################################################
#The following code performs input manipulation #
#################################################



fptr = open('mad_1.bff', 'r').read()
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

#print(grid)

blocks = {}

for line in raw_data:
	if line.startswith('A') == True or line.startswith('B') == True or line.startswith('C') == True:
		line = line.split()
		key = line[0]
		blocks[key] = int(line[1])

## First we will flatten the array into a 2D list for the sake of convenience and binning.

net_grid = [i for j in grid for i in j]

## Replacing the string vacancies to integers

#for n,i in enumerate(net_grid):
	#if i == 'o':
		#net_grid[n] = 0

print(net_grid)


def MC_Generator(net_grid, blocks, steps):
	'''
	This is a Monte Carlo based random board generator. We are using a Monte carlo methodology instead of
	the usual iterative recursive methodology because we believe that Monte carlo with some smart intelligent bias will be faster to parse.

	**Parameters**
		net_grid : *list,str*
			This is a list of strings stating the nature of the grid. Note that it is not a nested list.
		blocks : *dict*
			This is a dict which contains the data about the blocks classified by its type.
		steps : *int*
			The steps are the number of Monte Carlo steps you want to perform. Code needs to be rectified a bit to make sure that it 
			is unrelated to the number of decoy boards in the output.

	**Returns*
		ensemble : *list,str*
			This is a list of strings for now. Modifying the code incorporates running the program and testing it simultaneously so that
			we don't store anything in memory.

	'''

	
	nA = blocks['A']
	nC = blocks['C']
	ensemble = []

	count = 0

	for i in range(0,steps):

		nA = blocks['A']
		nC = blocks['C']

		rand_i = random.sample(range(0,len(net_grid)),3)
		new_grid = []
		print rand_i


		#for i in range(0,steps)


		# !!! This does not address the fixed blocks in game grid
		 
		for i in range(len(net_grid)):

			if net_grid[i] != 'x':
				if i in rand_i:
					if nA > 0 :
						new_grid.append('A')
						nA = nA-1
					elif nA ==0 and nC > 0 :
						new_grid.append('C')
						nC = nC-1
				else:
					new_grid.append('o')

			elif net_grid[i] == 'x':
				new_grid.append('x')

		
			#print(rand_i)
			#print(new_grid)

		ensemble.append(new_grid)
		#count += 1

	return ensemble


if __name__ == "__main__":

	ans = MC_Generator(net_grid, blocks, 10)

	## To get back the grid in the game format from the code

	for i in ans:
		A = [i[x:x+4] for x in range(0,len(i),4)]
		print(A)







