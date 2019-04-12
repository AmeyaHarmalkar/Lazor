
class Game :
	'''
	'''

	def __init__(self, filename):
		self.fptr = open(filename, 'r').read()

	def database(self):
		all_lines = self.fptr.split('\n')
		raw_data = []

		# Split raw data by line into a list
		for line in all_lines:
			if '#' not in line and line != '':
				raw_data.append(line)
		#print(raw_data)


		# Split list into sublists to facilitate extraction of data into grid, blocks, laser, and destination points


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


		## Generating the Laser direction tuple 

		lazor_start=[]
		lazor_path=[]

		for line in raw_data:
			lazor_direction=[]
			if 'L' in line:
				line = line.lstrip("L").split()
				if len(line) == 4 :
					for i in range(len(line)):
						if i < 2 :
							lazor_start.append(int(line[i]))
						else :
							lazor_direction.append(int(line[i]))
					lazor_path.append(tuple(lazor_direction))
		
				else :
					print("Does not match the expected format. Input error. Core Dump")


		## Generating the list of points through which the laser should pass

		pointer = []

		for line in raw_data:
			point_set = []
			if line.startswith('P') == True:
				line = line.lstrip("P").split()
				if len(line) == 2:
					for i in range(len(line)):
						point_set.append(int(line[i]))
					pointer.append(tuple(point_set))
				else :
					print("Does not match the expected format. Input error. Core Dump")


		## Generating the dictionary describing the blocks

		blocks = {}

		for line in raw_data:
			if line.startswith('A') == True or line.startswith('B') == True or line.startswith('C') == True:
				line = line.split()
				key = line[0]
				blocks[key] = int(line[1])

		return grid, lazor_start, lazor_path, pointer, blocks



if __name__ == "__main__":
	G = Game('mad_1.bff')
	grid_net, lazer_ini, lazer_pathway, points, blcks = G.database()

	print('Grid =', grid_net)
	print('Blocks =', blcks)
	print('Laser sets =', lazer_pathway)
	print('Lazer initial =', lazer_ini)
	print('Point sets =', points)

#G2 = Game('mad_1.bff')