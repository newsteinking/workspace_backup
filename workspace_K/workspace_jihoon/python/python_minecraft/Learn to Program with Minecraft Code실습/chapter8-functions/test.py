from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
blocktype=1
#===============================================================================
# mc.setBlocks(x+2,y,z+2,
#              x+4,y,z+4,blocktype)
#===============================================================================

mc.setBlocks(x+2,y,z+2,\
             x+4,y,z+4,blocktype)