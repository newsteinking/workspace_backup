from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time

#==========================================================================================
mushroom=39
wood=5
clear=0
#==========================================================================================

pos=logan.player.getPos()
msg='x:{},y:{},z:{}'.format(pos.x,pos.y,pos.z)
logan.postToChat(msg)

#==========================================================================================
x=pos.x
y=pos.y
z=pos.z
front=3
up=1
#==========================================================================================

logan.setBlock(x+front,y,z,clear)
logan.setBlock(x+front,y+up,z,clear)
time.sleep(2)

logan.setBlock(x+front,y,z,wood)
logan.setBlock(x+front,y+up,z,mushroom)

