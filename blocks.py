## Creating Class Obejcts for the blocks

class Block(object):
	'''
	This class defines the block object and classifies according to the character of each of the blocks.
	The characters of the blocks are :
	A : Reflect block = reflects the incoming laser
	B : Opaque block = stops the laser beam
	C : Refract block = refracts the laser beam so that it passes through as well as reflects

	We need the laser to basically either pass or reflect. If there is an opaque block, it won't do either.
	Let's create a boolean so that we can get all the four cases .i.e. with no pass, with pass and no reflect, 
	with reflect & no pass, and with reflect & pass

	**Parameters**

		x : the column numbering of the block
		y : the row numbering of the block

	'''

	def __init__(self,block):

		self.block = block
		
		if block == "A":
			self.through = False
			self.reflect = True
		elif block == "B":
			self.through = False
			self.reflect = False
		elif block == "C":
			self.through = True
			self.reflect = True
		else:
			self.through = True
			self.reflect = False



## Just a check!

O2 = Block('A').reflect
print(O2)
#print(O2.through)
