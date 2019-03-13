from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time

x,y,z=mc.player.getPos()
width=50
front=4
for i in range(width//2):
    mc.setBlocks(x+front+i,y+i,z+front+i,x+width+front-i,y+i,z+width+front-i,block.SAND.id)