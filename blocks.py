## Creating Class Objects for the blocks

class Blocks:
	class Reflect:
		def __init__(self,nA,x,y):
			self.amount = nA
			self.x = x
			self.y = y
		def prop(self):
			'''
			This function defines the property of laser path once it hits this block. 
			'''
			self.reflect = True
			self.transmit = False
			return self.reflect, self.transmit

	class Opaque:
		'''
		This class defines the Opaque block. For now I have just defined it so that it can define the positioning of the blocks.
		**Functions**
		__init__
		**Parameters**
			x : the column numbering of the block
			y : the row numbering of the block
		'''
		def __init__(self,nB,x,y):
			self.amount = nB
			self.x = x
			self.y = y
		def prop(self):
			self.reflect = False
			self.transmit = False
			return self.reflect, self.transmit

	class Refract:
		def __init__(self,nC,x,y):
			self.amount = nC
			self.x = x
			self.y = y
		def prop(self):
			self.reflect = True
			self.transmit = True
			return self.reflect, self.transmit

## Just a check!
if __name__ == "__main__":
	A = Blocks.Reflect(2,3,5)
	print(A.prop())