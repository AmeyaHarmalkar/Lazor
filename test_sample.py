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

## Generating the game grid

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



def Permutator(net_grid, blocks, reverse=False, allowEmpty=True):
	'''
	Generator to return the possible ways of distributing n distinguishable objects between k distinguishable bins.

	**Parameters**

		net_grid : *list,str*
			The grid defines the bin which we need to operate on.

		blocks : *dict*
			The dictionary indicating the type and number of blocks of a specific kind.

		reverse : *bool*
			If true, generates a reverse-order sequence. Default is kept False.

		allowEmpty : *bool*
			If true, empty bins are allowed. Default is true.

	'''

	if len(net_grid) < 1 or len(blocks) < 1:
		raise ValueError("Number of empty spaces and the blocks must be both greater than or equal to 1")

	lng = len(net_grid)
	lnb = len(blocks)

	bars = [([0]*(lng-lnb-5) + ['A']*blocks['A'] + ['C']*blocks['C'],1)]

	if reverse :

		print("I don't want to waste time doing reverse. Perform ascending mode instead!")

	else:

		#Generate the permutation boards in ascending order instead!

		# The plan is to iterate through the current queue of arrangements until no more arrangements are left!

		while len(bars) > 0:

			newbars = []

			#for b in bars:
				#We need t


lng = len(net_grid)
lnb = sum(blocks.values())

bars = [(['o']*(lng-lnb) + ['A']*blocks['A'] + ['C']*blocks['C'],1)]

print(bars[0])

import itertools
from itertools import *
def permutations1(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return



def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)
Ans = permutations(bars[0][0])


for i in list(set(Ans)):
	print(i)

#for b in bars:
#	print(b[0][-2])


#while len(bars) > 0:
#	newBars = []
#	for b in bars:
#		for x in range(b[0][-2], stars+1):
#			newBar = b[0][1:bins] + [x, stars]      
#			if b[1] < bins-1 and x > 0:
#				newBars.append((newBar, b[1]+1))
#			yield tuple(newBar[y] - newBar[y-1] + (0 if allowEmpty else 1) for y in range(1, bins+1))
#	bars = newBars



## Alternative method for trying out a different combination strategy. Irrelevant for now.

def weak_compositions(boxes, balls, parent=tuple()):
  if boxes > 1:
    for i in xrange(balls + 1):
      for x in weak_compositions(boxes - 1, i, parent + (balls - i,)):
        yield x
  else:
    yield parent + (balls,)

count = 0
for x in weak_compositions(5,3):
	count += 1
 	#print(x)

