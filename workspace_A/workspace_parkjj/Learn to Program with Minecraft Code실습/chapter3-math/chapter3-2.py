from mcpi.minecraft import Minecraft
logan=Minecraft.create()
from mcpi import block
import time


pos=logan.player.getPos()

#-----------------------------------------------------
x1=pos.x
y1=pos.y
z1=pos.z
length=2
front=2
wood=5
air=0
melon=103
water=9
lava=11
length2=length*2
ice=79
front2=front*2
fire=62
#-----------------------------------------------------

#logan.setBlocks(x1,y1,z1,x1+length,y1+front,z1+length,wood)
#logan.setBlocks(x1+front,y1,z1,x1+front,y1,z1+length,melon)
#logan.setBlocks(x1+front,y1,z1,x1+500,y1,z1+500,air)
logan.setBlocks(128,0,128,-128,-64,-128,80)
logan.setBlocks(x1+front,y1,z1,x1+front2,y1+length,z1+front,wood)
logan.setBlock(x1+front,y1+1,z1+1,fire)
logan.postToChat(3**4)