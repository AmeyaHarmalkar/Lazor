# Lazor
### 1. Introduction
*Lazor* is a mobile game available on [Android](https://play.google.com/store/apps/details?id=net.pyrosphere.lazors&hl=en_US) and [iOS](https://itunes.apple.com/us/app/lazors/id386458926?mt=8). To win, square blocks have to be positioned to direct the laser path through all the required intercepts. There are 3 types of blocks:<br/>
* Reflect: white block that reflects laser path
* Opaque: dark block that blocks laser path
* Refract: transparent block that both transmits the laser through and reflects it

In the base free game, only 3 hints are provided. The objective of this group project is to create a universal solver for *Lazor*.
### 2. Methodology
  ##### 1. Input
The input file .bff contains the following information: starting layout of the game grid, types and quantities of available blocks, laser sources and paths, and intercept positions.<br/>
x = no block allowed<br/>
o = blocks allowed<br/>
A = fixed reflect block<br/>
B = fixed opaque block<br/>
C = fixed refract block<br/>

Axes defining block, laser and intercept positioning are as followed:<br/>
  __________\ +x<br/>
 |          / <br/>
 |<br/>
 |<br/>
\|/ +y<br/>

  ##### 2. Solver
In each iteration, random positions on the board are chosen for block placement. Refract blocks are then selected first to randomly populate these positions, then reflect and finally opaque blocks. Because refract blocks split the laser path and there are typically fewer of them than reflect blocks, this serves to maximize the number of laser paths in fewer iterations and thus increasing the probability of getting the right solution. If the laser hits the edge of a block, depending on the block type and position relative to the laser trajectory, laser is reflected, transmitted, both, or stopped. A maximum number of iterations is provided to prevent indefinite calculations in case a solution takes too long or could not be found.
  ##### 3. Output
The solution is written in grid form (similar to input) in **solution.bff**.
### 3. Codes
Code is written using *Object-oriented Programming*. 5 class objects have been created:
* Game: import and parse data from .bff input file<br/>
  All data are parsed into lists of lists. Coordinates are converted to integers.
* Board: generate a new, more detailed grid for object placement and manipulation using information<br/>
  Coordinate system (*tuple*) starts at (0,0) in the top left corner. Each block pieces are 2 x 2 in the new grid and are placed in positions with odd coordinates. 
* Blocks: define properties of the 3 types of blocks with boolean
* Laser: algorithm for the game solver<br/>
At each position the laser passes through, a neighbor check is performed to determine if a block is in the immediate horizontal or vertical vicinity, which means that the laser just hits the edge of a block. The type of the block determines new laser paths.
* MyTest: unit test codes for various functions and components to ensure code functionality and facilitate debugging.

To solve for different levels, simply change the filename to something else at:
```solution_generator(game, maxiter)```
### 4. File organization
Codes were written in parts and assembled into a final file **lazor_solver.py**. 
### Authors:
Ameya Harmalkar https://github.com/AmeyaHarmalkar<br/>
Haonan Xu https://github.com/haonan-xu<br/>
Avery Tran https://github.com/AveryTran<br/>
Henry Herbol https://github.com/hherbol<br/>
