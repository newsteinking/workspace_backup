from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time

#x,y,z=mc.player.getPos()
pos=mc.player.getPos()
x,y,z=pos.x,pos.y,pos.z
front=5

for step in range(15):
    time.sleep(0.3)
    for i in range(3):
        mc.setBlock(x+front+step,y+step,z+i,block.IRON_BLOCK.id)
        time.sleep(0.3)