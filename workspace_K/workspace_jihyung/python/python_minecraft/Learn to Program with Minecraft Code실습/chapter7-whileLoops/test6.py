from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from mcpi import block
import time

x,y,z=mc.player.getPos()
front=3
blocktype=block.GOLD_BLOCK.id

for i in range(16):
    mc.setBlock(x+front+i,y+i,z,blocktype)
    #x=x+1
    time.sleep(1)
