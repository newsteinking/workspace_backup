from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time
x,y,z=mc.player.getPos()
front=7

for i in range(0,50,5):
    mc.setBlocks(x+front,y,z+i,x+front,y+7,z+i,block.WOOD.id)
    time.sleep(3)
    mc.setBlocks(x+front-1,y+8,z+i-1,x+front+1,y+8,z+i+1,block.LEAVES.id)
    time.sleep(3)