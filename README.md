# Lazor
# Lazor Code


Different classes and there definitions and purposes :

## 1. Class Game :

This class takes in the input data from the user-specified file, parses through it and converts everything in the format we need it to be in. 

Functions :

1. init : to open and read the files
Returns : none

2. database : to generate the database in the necessary format.
Returns : none
Methods :
* seld.grid = To generate a list of list of strings specifying positions which are open on the board
* self.lazor_start = To generate a list of tuples specifying the laser origin points.
* self.lazor_path = To generate a list of tuples specifying the direction of laser. Each element corresponds to the 
                  path of the respective origin laser point
* self.pointer = To generate a list of tuples indicating the points through which the laser should pass.
* self.blocks = To create a dictionary of the blocks specifying the count for each type of blocks.
