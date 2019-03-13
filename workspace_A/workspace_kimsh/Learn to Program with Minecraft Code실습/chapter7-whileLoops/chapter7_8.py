from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time

x,y,z=mc.player.getPos()
x1=x+1
x2=x+3
y-=1
z1=z+1
z2=z+3
blocktype=block.GOLD_BLOCK.id
mc.setBlocks(x1,y,z1,x2,y,z2,blocktype)
