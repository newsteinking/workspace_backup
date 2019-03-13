from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random

x,y,z=mc.player.getPos()

def randomblocklocation(blocktype,repeat):
    x,y,z=mc.player.getPos()
    for i in range(repeat):
        x=x+random.randrange(-20,20)
        z=z+random.randrange(-20,20)
        mc.setBlock(x,y,z,blocktype)
        
randomblocklocation(103,7)
randomblocklocation(56,7)
randomblocklocation(98,7)  