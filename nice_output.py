import random
import unittest




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
		with open(filename, 'r') as f:
			self.fptr = f.read()


	def database(self):
		'''
		This function takes in the input file and converts it into a format that will be used throughout the code.
		
		**Parameters**

			none

		**Returns**

			grid : *list,lsit,str* 
				A nested list of strings containing the description of the game board
			lazor_start : *list,tuple* 
				A list of tuples containing the origin data of lazor input.
			lazor_path : *list,tuples* 
				A list of tuples containing the path of the lazor .i.e. its direction.
			pointer : *list,tuples* 
				A list of tuples containing the position of the targets.
			blocks : *dict* 
				A dictionary with the types of blocks as keys and the number of blocks as values.

		'''


		all_lines = self.fptr.split('\n')
		raw_data = []

		# Split raw data by line into a list
		for line in all_lines:
			if '#' not in line and line != '':
				raw_data.append(line)

		# Split list into sublists to facilitate extraction of data into grid, blocks, laser, and destination points

		##############################
		## Generating the game grid ##
		##############################

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


		##########################################
		## Generating the Laser direction tuple ##
		##########################################

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



class Board:
	'''
	The class to generate the board game .i.e to create the meshgrid
	'''
	
	def __init__(self,grid,origin,path,sets):
		'''
		Just to assemble all the data, so that it can be called upon whenever.
		'''
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


		# Orderly insertion of the 3 blocks. First inserts the C blocks, then the A blocks and then the B blocks.
		# Would be more fun to randomly insert any block whatsoever.

		for element in options:
			(i,j) = element

			if nC != 0 :
				grid[j][i] = 'C'
				nC = nC-1
			
			else:
				if nA != 0 :
					grid[j][i] = 'A'
					nA = nA-1
				else :
					if nB != 0:
						grid[j][i] = 'B'
						nB = nB-1
					else:
						print("Some error")
		return grid

	def make_board(self,grid):
		'''
		The function to make the actual board through which the laser can parse through. It converts the sample_board of 
		dimension (i*j) to a board of dimensions (2i+1)*(2j+1). This is important as the lazor passes through the midpoints

		'''

		meshgrid = [['o' for i in range(2*len(grid[0])+1)] for j in range(2*len(grid)+1)]

		for i in range(len(grid)):
			for j in range(len(grid[0])):
				meshgrid[2*i+1][2*j+1] = grid[i][j]

		return meshgrid


class Blocks:
	'''
	This class defines the 'reflect' and 'transmit' properties for each position in the game board.
	'''
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def prop(self, meshgrid):
		'''
		This function specifies the 'reflect' and 'transmit' properties as booleans
		**Parameter**
			self.x: *int* - position row coordinate
			self.y: *int* - position column coordinate
		
		**Returns**
			self.reflect: *boolean* - whether the position reflects the laser
			self.transmit: *boolean* - whether the position allows laser to transmit through
		'''

		if meshgrid[self.y][self.x] == 'A':
			self.reflect = True
			self.transmit = False
		elif meshgrid[self.y][self.x] == 'B':
			self.reflect = False
			self.transmit = False
		elif meshgrid[self.y][self.x] == 'C':
			self.reflect = True
			self.transmit = True
		else:
			self.reflect = False
			self.transmit = True
		return self.reflect, self.transmit



class Laser:
	'''
	The laser class which stores the start position and the direction of the Laser.
	'''

	def __init__(self, start_point, path):
		self.source = start_point
		self.direction = path

	def pos_chk(x, y, nBlocks):
		return x >= 0 and x < nBlocks and y >= 0 and y < nBlocks

	def laser_strikes(self, path, intercepts, grid, meshgrid, path_1, intercept_new):
		'''
		The function to predict where a lazor beam will strike. This is a function that will analyze at each point of the lazor
		beam. It will check whether their are any block neighbours, what are the characteristics of those block neighbours and will
		perform suitable operations on them accordingly. 

		**Parameters**

			path : *list,tuple*
				A list of tuples containing the direction of the lazor.

			intercepts : *list,tuple*
				A list of tuples containing the intercepts through which the lazor beam passes through.

			grid : *list,list,str*
				A nested list of strings that denotes the positioning of the blocks in the game. Subset of meshgrid

			meshgrid : *list,list,str*
				A nested list of strings derived from the grid, indicating all the positions of the blocks as well as the
				positions/points, through which the lazor can pass through.

		**Returns**

			path, intercepts

		'''
		
		(dx, dy) = path[-1]

		# The last position of the laser
		(nx, ny) = intercepts[-1]


		# Directions to perform a check
		n_direct = [(0, 1),(0, -1),(-1, 0),(1, 0)]


		# Creating a buffer to check the surrounding positions

		nlist = []
		transmit_list = []

		# Exploring the neighbours of the new point to modify directions

		if (dx,dy) != (0,0):

		#This will allow the loop to proceed only if there is a viable direction to proceed	

			for i in range(len(n_direct)):
				
				ex = nx + n_direct[i][0]
				ey = ny + n_direct[i][1]

				if ex > 0 and ex < 2*len(grid[0])+1 and ey > 0 and ey < 2*len(grid)+1:
					#Just to perform a check that we are still within the grid
					delta_x = ex-nx
					delta_y = ey-ny

					#print(Blocks(ey,ex).prop(meshgrid))

					if Blocks(ex,ey).prop(meshgrid) == (True,False) :
						
					#if meshgrid[ey][ex] == 'A':

						if delta_x == dx or delta_y == dy:

							if delta_x == 0:
								new_dx = dx * 1
							else:
								new_dx = dx * -1
							if delta_y == 0:
								new_dy = dy * 1
							else:
								new_dy = dy * -1
							nlist.append((new_dx,new_dy))

						else:

							new_dx = dx * 1
							new_dy = dy * 1
							nlist.append((new_dx,new_dy))


					elif Blocks(ex,ey).prop(meshgrid) == (False,False) :
					#elif meshgrid[ey][ex] == 'B':

						if delta_x == dx or delta_y == dy:
							new_dx = dx * 0
							new_dy = dy * 0
						else :
							new_dx = dx * 1
							new_dy = dy * 1
						nlist.append((new_dx,new_dy))


					elif Blocks(ex,ey).prop(meshgrid) == (True,True) :
					#elif meshgrid[ey][ex] == 'C':

						if delta_x == dx or delta_y == dy:

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

						else:

							new_dx = dx * 1
							new_dy = dy * 1
							nlist.append((new_dx,new_dy))


			if len(nlist) > 0:
				# Needs a rectification here! Can't handle properly if there are 2 reflect blocks side-by-side.
				path.append(nlist[-1])

			else :
				path.append((dx,dy))

			if len(transmit_list) > 0 :
				path_1.append(transmit_list[-1])
				intercept_new.append((nx,ny))

			nx += path[-1][0]
			ny += path[-1][1]

			intercepts.append((nx,ny))


		return path,intercepts, path_1, intercept_new


	def trajectory(self, path, grid, meshgrid):

		#meshgrid = [['o' for i in range(2*len(grid[0])+1)] for j in range(2*len(grid)+1)]

		#print(meshgrid)


		intercepts = []
		path = []

		for i in range(len(self.source)):
			intercepts.append([self.source[i]])
			path.append([self.direction[i]])


		#intercepts = [tuple(self.source[0])]

		n_direct = [(0, 1),(0, -1),(-1, 0),(1, 0)]

		path_1 = []
		intercept_new = []
		#print(len(path_1))
		
		for k in range(len(path)) :

			# Perform an initial check at the input position to ensure that if there is a block in the neighbour domain of the
			# origin source, the direction of the laser will change right away.

			if len(intercepts[k]) == 1:

				path[k], intercepts[k], path_1, intercept_new = self.laser_strikes(path[k], intercepts[k], grid, meshgrid, path_1, intercept_new)

			# To continue the loop till the laser reaches the boundary of the grid.

			while intercepts[k][-1][0] != 0 and intercepts[k][-1][0] < len(meshgrid[0])-1 and intercepts[k][-1][1] != 0 and intercepts[k][-1][1] < len(meshgrid)-1:

				
				if path[k][-1] != (0,0) :

					path[k], intercepts[k], path_1, intercept_new = self.laser_strikes(path[k], intercepts[k], grid, meshgrid, path_1, intercept_new)

				else :
					
					break


			# To check whether if the Laser falls on any refract block, as it will split on collision and have 2 paths later on. 
			# The next 'if' conditional will allow to explore an additional path with the origin of the laser instantiated at the point 
			# of the split. It utilizes the function laser_strikes to explore the transmit path, considering that the split 
			# interface is now the origin

			if len(path_1) != 0:

				
				#print(path_1)
				path_0 = []
				intercept_0 = []
				
				(dx,dy) = path_1[-1]
				(cx, cy) = intercept_new[-1]

				nx = cx + dx
				ny = cy + dy

				intercept_new.append((nx,ny))
				
				while intercept_new[-1][0] != 0 and intercept_new[-1][0] < len(meshgrid[0])-1 and intercept_new[-1][1] != 0 and intercept_new[-1][1] < len(meshgrid)-1:
					


					if path_1[-1] != (0,0) :

						path_1, intercept_new, path_0, intercept_0 = self.laser_strikes(path_1, intercept_new, grid, meshgrid, path_0, intercept_0)

					else:
						break


		# The output will be in a nested list format. We want it to be in list form. I am hereby converting the nested list
		# into a list. This will be further useful as the testing function compares between 2 samples of list.
		final_intercept_list = []
		for sublist in intercepts:
			for item in sublist:
				final_intercept_list.append(item)



		return final_intercept_list, path, intercept_new





# Define a global function to solve the mesh

def outputter(mesh):

	print("Analyzing and preparing files for output...")

	solution = []

	for j in range(1,len(mesh), 2):
		for i in range(1, len(mesh[0]), 2):
			solution.append(mesh[j][i])

	width = int((len(mesh[0])-1) * 0.5)

	solution = [solution[x:x+width] for x in xrange(0, len(solution), width)]

	file = open('solution.bff', 'w')

	for i in solution:
		for j in i:
			file.write(j)
			file.write('\t')
		file.write('\n')
	file.close()

	print("Solution found!")




'''
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

	intercepts = []
	track = []

	for i in range(len(G.lazor_start)):
		intercepts.append([G.lazor_start[i]])
		track.append([G.lazor_path[i]])


	L = Laser(G.lazor_start,G.lazor_path)
	intcp, pth, intercept_new = L.trajectory(G.lazor_path,G.grid, mesh)

	#final_set = G.pointer

	#print(intcp)
	#print(intercept_new)
	#print(pth)

	#print(intercept_new)

	#total_intcp = intcp+intercept_new
	#print(total_intcp)

	#print(all(x in total_intcp for x in final_set))

###################################
	#print(B.sampler(G.grid))
	#print(B.sample_board(B.sampler(G.grid), G.blocks, G.grid))



for i in range(500000):
	G = Game('showstopper_4.bff')
	G.database()

	B = Board(G.grid,G.lazor_start, G.lazor_path,G.pointer)

	mesh = B.make_board(B.sample_board(B.sampler(G.grid), G.blocks, G.grid))

	#print(mesh)

	L = Laser(G.lazor_start,G.lazor_path)
	intcp, pth, intercept_new = L.trajectory(G.lazor_path,G.grid, mesh)
	final_set = G.pointer
	total_intcp = intcp+intercept_new
	##########
	#print(intcp)
	#print(intercept_new)
	#print(" ")
	#print(total_intcp)
	#print(" ")
	#print(final_set)
	#print("The solution is :")

	if all(x in total_intcp for x in final_set) == True:
		print("Yay")
		print(total_intcp)
		break

#print(final_set)


'''

## Outputs into a file

for i in range(100000):
	G = Game('dark_1.bff')
	G.database()

	B = Board(G.grid,G.lazor_start, G.lazor_path,G.pointer)

	mesh_board = B.sample_board(B.sampler(G.grid), G.blocks, G.grid)

	mesh = B.make_board(mesh_board)

	#mesh = B.make_board(B.sample_board(B.sampler(G.grid), G.blocks, G.grid))

	#print(mesh)

	L = Laser(G.lazor_start,G.lazor_path)
	intcp, pth, intercept_new = L.trajectory(G.lazor_path,G.grid, mesh)
	final_set = G.pointer
	total_intcp = intcp+intercept_new
	##########
	#print(intcp)
	#print(intercept_new)
	#print(" ")
	#print(mesh)
	#print(total_intcp)
	#print(" ")
	#print(final_set)
	#print("The solution is :")
	#outputter(mesh)

	if all(x in total_intcp for x in final_set) == True:
		print("Yay")
		print(intcp)
		print(intercept_new)
		print(total_intcp)
		mesh2 = mesh
		outputter(mesh2)
		print(" ")
		print(Blocks(3,5))
		
		break

(a,b) = Blocks(3,5).prop(mesh)
#print("Running the outputter")
if (a,b) == (True,True):
	print("Boom")

print("code finished running")





##########################################################################
##							UNIT TEST 									##
##########################################################################



class MyTest(unittest.TestCase):

	def test_game1(self):
		G1 = Game('dark_1.bff')
		G1.database()
		self.assertEqual(G1.grid, [['x', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'x']])
		self.assertEqual(G1.lazor_path, [(-1, 1), (1, -1), (-1, -1), (1, -1)])

	def test_game2(self):
		G2 = Game('tiny_5.bff')
		G2.database()
		self.assertEqual(G2.blocks, {'A': 3, 'C': 1, 'B': 0})
		self.assertEqual(G2.pointer, [(1, 2), (6, 3)])

	def test_game3(self):
		G3 = Game('yarn_5.bff')
		G3.database()
		self.assertEqual(G3.lazor_start, [(4, 1)])
		self.assertEqual(G3.grid, [['o', 'B', 'x', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'x', 'o', 'o', 'o'], ['o', 'x', 'o', 'o', 'x'], ['o', 'o', 'x', 'x', 'o'], ['B', 'o', 'x', 'o', 'o']])

	def test_sampler(self):
		G = Game('mad_4.bff')
		G.database()
		B = Board(G.grid,G.lazor_start, G.lazor_path,G.pointer)
		self.assertEqual(B.sampler(G.grid), [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2), (0, 3), (1, 3), (2, 3), (3, 3), (0, 4), (1, 4), (2, 4), (3, 4)])

	def test_blocks_1(self):
		G = Game('tiny_5.bff')
		G.database()
		B = Board(G.grid,G.lazor_start, G.lazor_path,G.pointer)
		mesh_board = B.sample_board(B.sampler(G.grid), G.blocks, G.grid)
		mesh = B.make_board(mesh_board)
		(a,b) = Blocks(3,1).prop(mesh)
		self.assertFalse(a)
		self.assertFalse(b)

	def test_blocks_2(self):
		G = Game('yarn_5.bff')
		G.database()
		B = Board(G.grid,G.lazor_start, G.lazor_path,G.pointer)
		mesh_board = B.sample_board(B.sampler(G.grid), G.blocks, G.grid)
		mesh = B.make_board(mesh_board)
		(a,b) = Blocks(1,11).prop(mesh)
		self.assertFalse(a)
		self.assertFalse(b)


if __name__ == '__main__':
	unittest.main()
