from mcpi.minecraft import Minecraft
from mcpi import block
import time
mc=Minecraft.create()
front=3

def make_block(x,y,z,Btype):
    if Btype==0:
        blocktype=0
        mc.setBlock(x,y,z,blocktype)
    else:
        blocktype=Btype
        mc.setBlock(x,y,z,blocktype)
    #blocktype=block.SNOW_BLOCK.id
    #mc.player.setPos(x,y,z)
    #mc.setBlock(x,y,z,blocktype)

x,y,z=mc.player.getPos() 
 
#===============================================================================
# make_block(x+front,y,z)
# make_block(x+front+1,y,z)
# make_block(x+front,y,z+1)
# make_block(x+front+1,y,z+1)
# make_block(x+front,y+1,z)
# make_block(x+front+1,y+1,z)
# make_block(x+front,y+1,z+1)
# make_block(x+front+1,y+1,z+1)
#===============================================================================

#===============================================================================
# for i in range(1,11):
#     make_block(x+front,y,z+i,0)
#     time.sleep(1)
#     make_block(x+front,y+1,z+i,0)
#     make_block(x+front,y,z+i,block.COAL_ORE.id)
#     time.sleep(1)
#     make_block(x+front,y+1,z+i,block.CLAY.id)
#===============================================================================

for i in range(1,6):
    make_block(x+front,y,z+i,0)
for i in range(1,6):
    make_block(x+front,y+1,z+i,0)
for i in range(1,6):
    make_block(x+front,y,z+i,block.GOLD_ORE.id)
    time.sleep(0.3)
for i in range(1,6):
    make_block(x+front,y+1,z+i,block.GOLD_BLOCK.id)
    time.sleep(0.1)
    
#===============================================================================
# int  hello()
# {
# }
# 
# hello();
#===============================================================================