from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
import time
 
def randomblocklocation(blocktype,repeat):
    x,y,z=mc.player.getPos()
    for i in range(repeat):
        x=x+random.randrange(-20,20)
        y=y+random.randrange(0,5)
        z=z+random.randrange(-20,20)
        mc.setBlock(x,y,z,blocktype)
        time.sleep(1)
randomblocklocation(2,20)
randomblocklocation(1,20)