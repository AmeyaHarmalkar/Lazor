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

print(grid)


blocks = {}

for line in raw_data:
	if line.startswith('A') == True or line.startswith('B') == True or line.startswith('C') == True:
		line = line.split()
		key = line[0]
		blocks[key] = int(line[1])

## First we will flatten the array into a 2D list for the sake of convenience and binning.

net_grid = [i for j in grid for i in j]

## Replacing the string vacancies to integers

for n,i in enumerate(net_grid):
	if i == 'o':
		net_grid[n] = 0

print(net_grid)

def Permutator(net_grid, blocks, reverse=False, allowEmpty=True):
	'''
	Generator to return the possible ways of distributing n distinguishable objects between k distinguishable bins
	'''