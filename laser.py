



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

for line in grid_raw:
	if line in raw_data:
		raw_data.remove(line)

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



class Laser:
	'''
	The laser class which stores the start position and the direction of the Laser.
	'''

	def __init__(self, start_point, path):
		self.source = start_point
		self.direction = path

	def pos_chk(x, y, nBlocks):
		return x >= 0 and x < nBlocks and y >= 0 and y < nBlocks

	def trajectory(self,path, grid):

		#meshgrid = [[0 for i in range(2*len(grid)+1)] for j in range(2*len(grid)+1)]
		meshgrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 'A', 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 'A', 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 'A', 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
		intercepts = [tuple(self.source)]

		n_direct = [(0, 1),(0, -1),(-1, 0),(1, 0)]

		
		
		while intercepts[-1][0] != 0 and intercepts[-1][0] != 8 and intercepts[-1][1] != 0 and intercepts[-1][1] != 8:

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

			# Exploring the neighbours of the new point to modify directions

			for i in range(len(n_direct)):
				ex = nx + n_direct[i][0]
				ey = ny + n_direct[i][1]

				if ex > 0 and ex < 2*len(grid)+1 and ey > 0 and ey < 2*len(grid)+1:
					#Just to perform a check that we are still within the grid
					delta_x = ex-nx
					delta_y = ey-ny

					# print("X",ex,nx,delta_x)
					# print("Y",ey,ny,delta_y)


					if meshgrid[ex][ey] == 'A':
						if delta_x == 0:
							new_dx = dx * 1
						else:
							new_dx = dx * -1
						if delta_y == 0:
							new_dy = dy * 1
						else:
							new_dy = dy * -1
						path.append((new_dx,new_dy))

					elif meshgrid[ex][ey] == 'B':
						new_dx = dx * 0
						new_dy = dy * 0
						path.append((new_dx,new_dy))


					elif meshgrid[ex][ey] == 'C':
						if delta_x == 0:
							new_dx = dx * 1
						else:
							new_dx = dx * -1
						if delta_y == 0:
							new_dy = dy * 1
						else:
							new_dy = dy * -1
						path.append((new_dx,new_dy))

					else:
						path.append((dx,dy))

			# print(path[-1])

		return intercepts, path





#meshgrid = [[0 for i in range(2*len(grid)+1)] for j in range(2*len(grid)+1)]
#meshgrid[1][5] = 'A'
#meshgrid[5][1] = 'C'
#meshgrid[7][3] = 'A'
#meshgrid2 = meshgrid
#print(meshgrid2)

print lazor_start
print lazor_path


A = Laser(lazor_start,lazor_path)

intcp, pth = A.trajectory(lazor_path,grid)

print(intcp)
print(pth)

