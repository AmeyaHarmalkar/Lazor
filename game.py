
class Game :
	'''
	This is the game grid. We have made this section to read user input, format and output it as per our
	requirements, to determine all the possible different combinations of boards we can make and run 
	a program through all of them to try and find a winning program!
	'''

	def __init__(self, filename):
		'''
		This is just an initialization function to enter the file into the system.

		**Parameters**

			filename : *str* 
				The name of the input file

		'''
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

		self.grid = []

		for i in grid_raw:
			trial_list = []
			x = ''.join(i.split())
			for letter in x:
				trial_list.append(letter)
			self.grid.append(trial_list)

		for line in grid_raw:
			if line in raw_data:
				raw_data.remove(line)


		## Generating the Laser direction tuple 

		self.lazor_start=[]
		self.lazor_path=[]

		for line in raw_data:
			lazor_direction=[]
			if 'L' in line:
				line = line.lstrip("L").split()
				if len(line) == 4 :
					for i in range(len(line)):
						if i < 2 :
							self.lazor_start.append(int(line[i]))
						else :
							lazor_direction.append(int(line[i]))
					self.lazor_path.append(tuple(lazor_direction))
		
				else :
					print("Does not match the expected format. Input error. Core Dump")


		## Generating the list of points through which the laser should pass

		self.pointer = []

		for line in raw_data:
			point_set = []
			if line.startswith('P') == True:
				line = line.lstrip("P").split()
				if len(line) == 2:
					for i in range(len(line)):
						point_set.append(int(line[i]))
					self.pointer.append(tuple(point_set))
				else :
					print("Does not match the expected format. Input error. Core Dump")


		## Generating the dictionary describing the blocks

		self.blocks = {}

		for line in raw_data:
			if line.startswith('A') == True or line.startswith('B') == True or line.startswith('C') == True:
				line = line.split()
				key = line[0]
				self.blocks[key] = int(line[1])

	def generate_boards(self):
		'''
		This function is to generate all the possible combinations of boards that can be parsed through with the 
		available blocks. 
		'''





if __name__ == "__main__":
	G = Game('yarn_5.bff')
	G.database()

	print('Grid =', G.grid)
	print('Blocks =', G.blocks)
	print('Laser path =', G.lazor_path)
	print('Lazer initial =', G.lazor_start)
	print('Point sets =', G.pointer)
