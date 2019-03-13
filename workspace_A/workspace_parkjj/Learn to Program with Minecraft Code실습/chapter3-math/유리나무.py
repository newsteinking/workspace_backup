from mcpi.minecraft import Minecraft
gt=Minecraft.create()
import time

pos=gt.player.getPos()

#===============================================       ======/
grass=2
wood=17
miniwood=6
x1=pos.x
y1=pos.y
z1=pos.z
leaf=1
up=1
upup=2
many_up=3
x2=pos.x-2
air=0
#================================================       ======/

gt.setBlocks(x1-1,y1-1,z1+4,x1+1,y1-1,z1+6,grass)
gt.setBlock(x1+3,y1,z1,miniwood)
time.sleep(1.5)
gt.postToChat("magic!!")
#MAKE MNIWOOD

gt.setBlocks(x2,y1+3,z1+2,x2+4,y1+4,z1+6,leaf)
gt.setBlock(x2,y1+3,z1+2,air)
gt.setBlocks(x2+4,y1+3,z1+2,x2+4,y1+4,z1+2,air)
gt.setBlock(x2+4,y1+3,z1+6,air)
gt.setBlocks(x1,y1+5,z1+3,x1+4,y1+6,z1+5,leaf)
gt.setBlocks(x2-1,y1+5,z1+4,x2+1,y1+6,z1+4,leaf)
gt.setBlocks(x1,y1,z1+4,x1,y1+4,z1+4,wood)