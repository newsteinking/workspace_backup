from mcpi.minecraft import Minecraft
from itertools import count
mc=Minecraft.create()
import time

x,y,z=mc.player.getPos()
front=2
blocks=[1,103,1,103,1,103,1,103,1,103]
#===============================================================================
# mc.setBlock(x+front,y,z+front,blocks[0])
# mc.setBlock(x+front,y+1,z+front,blocks[1])
# mc.setBlock(x+front,y+2,z+front,blocks[2])
# mc.setBlock(x+front,y+3,z+front,blocks[3])
# mc.setBlock(x+front,y+4,z+front,blocks[4])
# mc.setBlock(x+front,y+5,z+front,blocks[5])
# mc.setBlock(x+front,y+6,z+front,blocks[6])
# mc.setBlock(x+front,y+7,z+front,blocks[7])
# mc.setBlock(x+front,y+8,z+front,blocks[8])
# mc.setBlock(x+front,y+9,z+front,blocks[9])
#===============================================================================

#===============================================================================
# for i in range(len(blocks)):
#     mc.setBlock(x+front,y+i,z+front,blocks[i])
#===============================================================================
    
#===============================================================================
# count=0
# while count<10:
#      mc.setBlock(x+front,y+count,z+front,blocks[count])
#      count+=1  #count=count+1
#===============================================================================