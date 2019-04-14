import random


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
			lazor_direction = []
			lazor_origin = []
			if 'L' in line:
				line = line.lstrip("L").split()
				if len(line) == 4 :
					for i in range(len(line)):
						if i < 2 :
							lazor_origin.append(int(line[i]))
						else :
							lazor_direction.append(int(line[i]))
					self.lazor_start.append(tuple(lazor_origin))
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
		if 'A' not in self.blocks:
			self.blocks['A'] = 0
		if 'B' not in self.blocks:
			self.blocks['B'] = 0
		if 'C' not in self.blocks:
			self.blocks['C'] = 0

	def generate_boards(self):
		'''
		This function is to generate all the possible combinations of boards that can be parsed through with the 
		available blocks. 
		'''


class Board:
	'''
	The class to generate the baord game and all its various possibilities
	'''
	
	def __init__(self,grid,origin,path,sets):

		self.grid = grid

		self.origin = origin

		self.path = path

		self.sets = sets

	def sampler(self, grid):

		sample_space = []

		for j in range(len(grid)):
			for i in range(len(grid[0])):
				if grid[j][i] == 'o':
					sample_space.append(tuple((i,j)))
					
		return sample_space

	def sample_board(self, sample_space, blocks, grid):

		options = random.sample(sample_space, sum(blocks.values()))
		nA = blocks['A']
		nB = blocks['B']
		nC = blocks['C']

		for element in options:
			(i,j) = element

			if nA != 0 :
				grid[j][i] = 'A'
				nA = nA-1
			
			else:
				if nB != 0 :
					grid[j][i] = 'B'
					nB = nB-1
				else :
					if nC != 0:
						grid[j][i] = 'C'
						nC = nC-1
					else:
						print("Some error")
		return grid

	def make_board(self,grid):
		'''
		The function to make the actual board through which the laser can parse through
		'''

		meshgrid = [['o' for i in range(2*len(grid[0])+1)] for j in range(2*len(grid)+1)]

		for i in range(len(grid)):
			for j in range(len(grid[0])):
				meshgrid[2*i+1][2*j+1] = grid[i][j]

		return meshgrid



class Laser:
	'''
	The laser class which stores the start position and the direction of the Laser.
	'''

	def __init__(self, start_point, path):
		self.source = start_point
		self.direction = path

	def pos_chk(x, y, nBlocks):
		return x >= 0 and x < nBlocks and y >= 0 and y < nBlocks

	def trajectory(self,path, grid, meshgrid):

		#meshgrid = [['o' for i in range(2*len(grid[0])+1)] for j in range(2*len(grid)+1)]

		#print(meshgrid)

		intercepts = [tuple(self.source[0])]

		n_direct = [(0, 1),(0, -1),(-1, 0),(1, 0)]

		path_1 = []
		intercept_new = []
		#print(len(path_1))
		
		
		while intercepts[-1][0] != 0 and intercepts[-1][0] < len(meshgrid[0])-1 and intercepts[-1][1] != 0 and intercepts[-1][1] < len(meshgrid)-1:


			# The Directional path of the Laser beam
			(dx, dy) = path[-1]

			# The last position of the laser
			(cx, cy) = intercepts[-1]

			# Finding the next point 

			nx = cx + dx
			ny = cy + dy

			#print((nx,ny))

			intercepts.append((nx,ny))

			# Creating a buffer to check the surrounding positions

			nlist = []
			transmit_list = []

			# Exploring the neighbours of the new point to modify directions

			if (dx,dy) != (0,0):

			#This will allow the loop to proceed only if there is a viable direction to proceed	

				for i in range(len(n_direct)):
					ex = nx + n_direct[i][0]
					ey = ny + n_direct[i][1]

					if ex > 0 and ex < 2*len(grid)+1 and ey > 0 and ey < 2*len(grid)+1:
						#Just to perform a check that we are still within the grid
						delta_x = ex-nx
						delta_y = ey-ny

						if meshgrid[ex][ey] == 'A':
							if delta_x == 0:
								new_dx = dx * 1
							else:
								new_dx = dx * -1
							if delta_y == 0:
								new_dy = dy * 1
							else:
								new_dy = dy * -1
							nlist.append((new_dx,new_dy))


						elif meshgrid[ex][ey] == 'B':
							new_dx = dx * 0
							new_dy = dy * 0
							nlist.append((new_dx,new_dy))


						elif meshgrid[ex][ey] == 'C':
							if delta_x == 0:
								new_dx = dx * 1
							else:
								new_dx = dx * -1
							if delta_y == 0:
								new_dy = dy * 1
							else:
								new_dy = dy * -1
							old_dx = dx
							old_dy = dy
							transmit_list.append((old_dx,old_dy))
							nlist.append((new_dx,new_dy))


				if len(nlist) > 0:
					path.append(nlist[-1])

				else :
					path.append((dx,dy))

				if len(transmit_list) > 0 :
					path_1.append(transmit_list[-1])
					intercept_new.append((nx,ny))

				#print(path[-1])
			else :
				break

		# To check whether if the Laser falls on any refract block, as it will have an altered path later on. 
		# The next if code will allow to explore an additional path with the origin of the laser instantiated at the point of the
		# split

		if len(path_1) != 0:

			while intercept_new[-1][0] != 0 and intercept_new[-1][0] < len(meshgrid[0])-1 and intercept_new[-1][1] != 0 and intercept_new[-1][1] < len(meshgrid)-1:

				(dx, dy) = path_1[-1]

				# The last position of the laser
				(cx, cy) = intercept_new[-1]

				# Finding the next point 

				nx = cx + dx
				ny = cy + dy

				#print((nx,ny))

				intercept_new.append((nx,ny))

				# Creating a buffer to check the surrounding positions

				nlist = []
				transmit_list = []

				# Exploring the neighbours of the new point to modify directions

				if (dx,dy) != (0,0):

				#This will allow the loop to proceed only if there is a viable direction to proceed	

					for i in range(len(n_direct)):
						ex = nx + n_direct[i][0]
						ey = ny + n_direct[i][1]

						if ex > 0 and ex < 2*len(grid)+1 and ey > 0 and ey < 2*len(grid)+1:
							#Just to perform a check that we are still within the grid
							delta_x = ex-nx
							delta_y = ey-ny

							if meshgrid[ex][ey] == 'A':
								if delta_x == 0:
									new_dx = dx * 1
								else:
									new_dx = dx * -1
								if delta_y == 0:
									new_dy = dy * 1
								else:
									new_dy = dy * -1
								nlist.append((new_dx,new_dy))


							elif meshgrid[ex][ey] == 'B':
								new_dx = dx * 0
								new_dy = dy * 0
								nlist.append((new_dx,new_dy))


							elif meshgrid[ex][ey] == 'C':
								if delta_x == 0:
									new_dx = dx * 1
								else:
									new_dx = dx * -1
								if delta_y == 0:
									new_dy = dy * 1
								else:
									new_dy = dy * -1
								old_dx = dx
								old_dy = dy
								transmit_list.append((old_dx,old_dy))
								nlist.append((new_dx,new_dy))


					if len(nlist) > 0:
						path.append(nlist[-1])

					else :
						path.append((dx,dy))

					#print(path[-1])
				else :
					break



		return intercepts, path, intercept_new




if __name__ == "__main__":
	G = Game('mad_1.bff')
	G.database()

	#print('Grid =', G.grid)
	#print('Blocks =', G.blocks)
	#print('Laser path =', G.lazor_path)
	#print('Lazer initial =', G.lazor_start)
	#print('Point sets =', G.pointer)


	B = Board(G.grid,G.lazor_start, G.lazor_path,G.pointer)

	mesh = B.make_board(B.sample_board(B.sampler(G.grid), G.blocks, G.grid))

	#mesh = B.make_board(G.grid)

	#print(mesh)

	L = Laser(G.lazor_start,G.lazor_path)
	intcp, pth, intercept_new = L.trajectory(G.lazor_path,G.grid, mesh)

	print(intcp)
	print(pth)

	print(intercept_new)

	print(intcp+intercept_new)

	#print(B.sampler(G.grid))
	#print(B.sample_board(B.sampler(G.grid), G.blocks, G.grid))


