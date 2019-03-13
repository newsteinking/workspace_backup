from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from mcpi import block
import time

mc.postToChat("test")
count=0
#===============================================================================
# while count <5:
#     mc.postToChat("test2")
#     time.sleep(1)
#     mc.postToChat(count)
#     count=count+1
#     
#===============================================================================

#===============================================================================
# for i in range(0,5):
#     mc.postToChat(i)
#     time.sleep(1)
#===============================================================================

x,y,z=mc.player.getPos()
front=3
width=50
blocktype=block.SANDSTONE.id

for i in range(50//2):
    mc.setBlocks(x+front+i,y+i,z+i,x+front+width-i,y+i,z+width-i,blocktype)
    
