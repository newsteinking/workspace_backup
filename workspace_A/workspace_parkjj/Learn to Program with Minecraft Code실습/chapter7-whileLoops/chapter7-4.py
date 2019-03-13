from mcpi.minecraft import Minecraft
import time
import random
from mcpi import block
logan=Minecraft.create()

logan.player.setPos(1,1,1)
while True:
    pos=logan.player.getPos()
    x0=pos.x
    y=pos.y
    z0=pos.z
    x=x0+random.randrange(1,10)
    z=z0+random.randrange(1,10)
    logan.player.setPos(x,y,z)
    logan.setBlock(x,y-1,z,103)
    pos=logan.player.getPos()
    x0=pos.x
    y=pos.y
    z0=pos.z
    if x0 > 128:
        logan.player.setPos(1,1,1)
        
    elif z0 > 128:
        logan.player.setPos(1,1,1)
    
    else:
        time.sleep(1)