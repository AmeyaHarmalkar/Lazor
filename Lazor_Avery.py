'''

'''

def data(filename):
	'''

	'''

	# Extract raw data from .bff file
	fptr = open(filename, 'r').read()
	all_lines = fptr.split('\n')
	raw_data = []

	# Split raw data by line into a list
	for line in all_lines:
		if '#' not in line and line != '':
			raw_data.append(line)

	# Split list into sublists to facilitate extraction of data into grid, blocks, laser, and destination points
	setup = fptr.split('\n')[9:]
	grid_start = raw_data.index('GRID START')
	grid_stop = raw_data.index('GRID STOP')

	grid_raw = raw_data[grid_start+1:grid_stop]
	setup = raw_data[grid_stop+1:]
	
	# Extract from raw data information on grid, blocks, laser and points:
	grid, laser, point = [], [], []
	blocks = setup[:]

	for g in grid_raw:
		x = ''.join(g.split())
		grid.append(x)

	for line in setup:
		if 'L' in line:
			laser.append(line)
			blocks.remove(line)
			continue
		elif 'P' in line:
			point.append(line)
			blocks.remove(line)

	return raw_data, grid, blocks, laser, point

if __name__ == "__main__":
	raw, grid, blocks, laser, point = data('mad_1.bff')
	print(raw, grid, blocks, laser, point, sep='\n')
