from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from mcpi import block
import time

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z

height=mc.getHeight(x,z)

mc.postToChat(height)
mc.postToChat(y)

ground= y >= height

if ground ==True:
    print("I ams in air")
    mc.postToChat("I am in air")
else:
    print("I ams in ground")
    mc.postTochat("I am in ground")
    
    
mc.postToChat(ground)

front=3
height=1
#blocktype=block.SNOW.id
blocktype=103
for i in range(6):
    time.sleep(1)
    mc.setBlock(x+front,y,z+i,blocktype)
time.sleep(2)  

blocktype=103
for i in range(6):
    time.sleep(1)
    mc.setBlock(x+front,y+height,z+i,blocktype)
 
blocktype=0
for i in range(6):
    time.sleep(1)
    mc.setBlock(x+front,y,z+i,blocktype)    




#===============================================================================
# blocktype=103
# mc.setBlock(x+front,y,z,blocktype)
# mc.setBlock(x+front,y,z+1,blocktype)
# mc.setBlock(x+front,y,z+2,blocktype)
# mc.setBlock(x+front,y,z+3,blocktype)
# mc.setBlock(x+front,y,z+4,blocktype)
# time.sleep(3)
# blocktype=0
#===============================================================================

#===============================================================================
# mc.setBlock(x+front,y,z,blocktype)
# mc.setBlock(x+front,y,z+1,blocktype)
# mc.setBlock(x+front,y,z+2,blocktype)
# mc.setBlock(x+front,y,z+3,blocktype)
# mc.setBlock(x+front,y,z+4,blocktype)
#===============================================================================



