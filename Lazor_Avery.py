'''

'''

def data(filename):
	'''
	This function extracts raw data from .bff input file
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
	grid, laser_raw, point_raw = [], [], []
	blocks = setup[:]

	for g in grid_raw:
		x = ''.join(g.split())
		grid.append(x)

	for line in setup:
		if 'L' in line:
			laser_raw.append(line)
			blocks.remove(line)
			continue
		elif 'P' in line:
			point_raw.append(line)
			blocks.remove(line)

	return grid, blocks, laser_raw, point_raw

def laser_prop(laser_raw):
	'''
	This function returns laser properties as a list of integers.
	'''
	
	# laser_x, laser_y, laser_vx, laser_vy = [], [], [], []
	laser_trim = []
	for source in laser_raw:
		for i in range(2, len(source)):
			if source[i] != ' ' and source[i] != '-':
				if source[i-1] == '-':
					value = int(source[i-1] + source[i])
					laser_trim.append(value)
				else:
					laser_trim.append(int(source[i])) 
	return laser_trim
			# laser_x.append(source[2])
			# laser_y.append(source[4])
			# laser_vx.append(source[6])
			# laser_vy.append(source[8])
	# return laser_x, laser_y, laser_vx, laser_vy

class Blocks:
	def __init__(self, amount):
		self.amount = amount
	def info(self):
		pass

if __name__ == "__main__":
	grid, blocks, laser, point = data('dark_1.bff')
	laser_prop = laser_prop(laser)
	# laser_x, laser_y, laser_vx, laser_vy = laser_prop(laser)
	print(grid, blocks, laser, point, laser_prop, sep='\n')
	# print(laser_x, laser_y, laser_vx, laser_vy, sep='\n')
