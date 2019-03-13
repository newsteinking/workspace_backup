from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from mcpi import block
import time

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
blocktype=block.CLAY.id
front=3

mc.setBlock(x+front,y,z,blocktype)
BlockCheck=mc.getBlock(x+front,y,z)
print(BlockCheck)

time.sleep(1)

if BlockCheck==block.CLAY.id :
    mc.postToChat("Your block number is 82.")
    
else:
    mc.postToChat("Your block number isn't 82.")