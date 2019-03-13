from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
import random

x,y,z=mc.player.getPos()
# pos is tuple type
pos=mc.player.getPos()
print(pos)
poslist=list(pos)
print(poslist)
front=10
blocktype=103
def getblocktype():
    blocks=[103,2,3,12,13,14,15]
    ablock=random.choice(blocks)
    return ablock

width=10
x+=10
for i in range(5):
    print(i)
    mc.setBlocks(x-i,y+i,z-i,x+i,y+i,z+i,12)
