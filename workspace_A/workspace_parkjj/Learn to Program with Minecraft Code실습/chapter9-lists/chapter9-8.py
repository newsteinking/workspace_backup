from mcpi.minecraft import Minecraft
import time
import random
logan=Minecraft.create()
x,y,z=logan.player.getPos()
while True:
    blocks=[11,9]
    block=random.choice(blocks)
    logan.setBlock(x+2,y,z,block)
#61,82,22,112,20,81,54,7,35,30