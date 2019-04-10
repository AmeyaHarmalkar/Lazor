'''

'''

def data(filename):
	fptr = open(filename, 'r').read()
	all_lines = fptr.split('\n')
	raw_data = []
	for line in all_lines:
		if '#' not in line and line != '':
			raw_data.append(line)

	setup = fptr.split('\n')[9:]
	grid_start = raw_data.index('GRID START')
	grid_stop = raw_data.index('GRID STOP')

	grid_raw = raw_data[grid_start+1:grid_stop]
	grid = []
	for g in grid_raw:
		x = ''.join(g.split())
		grid.append(x)
	setup[:] = (line for line in setup if line != '')

	return grid

if __name__ == "__main__":
	grid = data('mad_1.bff')
	print(grid)
	# print(line, grid, '\n', setup, sep = '')
