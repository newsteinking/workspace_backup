from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time

time.sleep(10)
hitt=mc.events.pollBlockHits()
#===============================================================================
# print(hitt)
# 
# for a in hitt:
#     print(a)
#     print(a.pos.x)
#     print(a.pos.y)
#     print(a.pos.z)
#===============================================================================
for a in hitt:
    x,y,z=a.pos.x,a.pos.y,a.pos.z
    mc.setBlock(x,y,z,block.DIAMOND_BLOCK.id)