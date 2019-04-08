'''

'''

def data(filename):
	fptr = open(filename, 'r').read()
	grid = fptr.split('\n')[4:7]
	setup = fptr.split('\n')[9:]
	# block = []
	# for x in setup[:3]:
	# 	if x[0] == 'A':
	# 		A = int(x[2])
	# 	elif x[0] == 'B':
	# 		B = int(x[2])
	# 	elif x[0] == 'C':
	# 		C = int(x[2])
	return grid, setup

if __name__ == "__main__":
	grid, setup = data('dark_1.bff')
	# print(B)
	print(grid, '\n', setup, sep = '')
