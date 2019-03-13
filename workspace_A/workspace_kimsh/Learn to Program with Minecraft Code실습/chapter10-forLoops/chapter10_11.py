from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time
x,y,z=mc.player.getPos()
front=5
blocktype=block.SANDSTONE.id
#levels=reversed(range(4))
#print(levels)

levels=reversed(range(4))
for i in levels:
    mc.setBlocks(x+front+i,y,z+i,x+front-i,y,z-i,blocktype)
    y+=1