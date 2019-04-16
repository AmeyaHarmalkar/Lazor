# # Just a test meshgrid
# meshgrid = [['x', 'o', 'o'], ['o','A','o'],['o','B','x']]

class Blocks:
	'''
	This class defines the 'reflect' and 'transmit' properties for each position in the game board.
	'''
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def prop(self):
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

# Just a check!
if __name__ == "__main__":
	# pos = Blocks(1,2)
	# print(pos.prop())
	pass