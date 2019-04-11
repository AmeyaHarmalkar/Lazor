## Creating Class Obejcts for the blocks

class Opaque:
	'''
	This class defines the Opaque block. For now I have just defined it so that it can define the positioning of the blocks.

	**Functions**

	__init__

	**Parameters**

		x : the column numbering of the block
		y : the row numbering of the block


	'''
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Reflect:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Refract:
	def __init__(self,x,y):
		self.x = x
		self.y = y


## Just a check!

O2 = Opaque(2,4)
print(O2.x)
print(O2.y)

