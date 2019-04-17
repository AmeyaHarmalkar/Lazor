# Lazor
### 1. Introduction
*Lazor* is a mobile game available on [Android](https://play.google.com/store/apps/details?id=net.pyrosphere.lazors&hl=en_US) and [iOS](https://itunes.apple.com/us/app/lazors/id386458926?mt=8). To win, square blocks have to be positioned to direct the laser path through all the required intercepts. There are 3 types of blocks:
* Reflect: white block that reflects laser path
* Opaque: dark block that blocks laser path
* Refract: transparent block that both transmits the laser through and reflects it

In the base free game, only 3 hints are provided. The objective of this group project is to create a universal solver for *Lazor*.
### 2. Methodology
#### 1. Input
        The input file .bff contains the following information: starting layout of the game grid, types and quantities of available blocks, laser sources and paths, and intercept positions. 
x = no block allowed
o = blocks allowed
A = fixed reflect block
B = fixed opaque block
C = fixed refract block

x, y, vx, vy
Axes defining block, laser and intercept positioning are as followed:
      __________\ +x
      |         /
      |
      |
      |
     \|/ +y

### 3. Codes
### 4. Branch organization
### Authors:
Henry Herbol https://github.com/hherbol<br/>
Ameya Harmalkar https://github.com/AmeyaHarmalkar<br/>
Antonio Xu https://github.com/haonan-xu<br/>
Avery Tran https://github.com/AveryTran<br/>

import Lazor


if __name__ = __main__:
  lazor.run()
