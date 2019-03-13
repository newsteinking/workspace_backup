from mcpi.minecraft import Minecraft
from mcpi import block
import random
mc=Minecraft.create()
import time

mc.postToChat("Test")
blocktype=block.CLAY.id
count=1
while count<5:
    x=random.randrange(0,50)
    y=random.randrange(4,20)
    z=random.randrange(0,50)
    mc.postToChat(count)
    mc.postToChat("x:{},y:{},z:{}".format(x,y,z))
    mc.player.setPos(x,y,z)
    mc.setBlock(x,y,z,blocktype)
    count+=1
    time.sleep(1)