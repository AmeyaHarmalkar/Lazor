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
	setup = raw_data[grid_stop+1:]
	
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


	# block = []
	# for x in setup[:3]:
	# 	if x[0] == 'A':
	# 		A = int(x[2])
	# 	elif x[0] == 'B':
	# 		B = int(x[2])
	# 	elif x[0] == 'C':
	# 		C = int(x[2])
	return grid, blocks, laser, point

if __name__ == "__main__":
	grid, blocks, laser, point = data('mad_1.bff')
	print(grid, blocks, laser, point, sep='\n')
