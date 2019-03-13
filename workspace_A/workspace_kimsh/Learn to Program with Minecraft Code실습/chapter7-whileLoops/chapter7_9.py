from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time

x,y,z=mc.player.getPos()
x1=x-1
x2=x+2
y=y-1
z1=z-1
z2=z+2
blocktype=block.SANDSTONE.id
mc.setBlocks(x1,y,z1,x2,y,z2,blocktype)
while x1<x<x2 and z1<z<z2:
    mc.postToChat("your on the sandstone.")
    time.sleep(3)
    x,y,z=mc.player.getPos()
    