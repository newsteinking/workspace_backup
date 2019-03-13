from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from mcpi import block
x,y,z=mc.player.getPos()
front=2
width=3
depth=3
blocktype=block.GOLD_ORE.id

#===============================================================================
# mc.setBlocks(x+front,y,z,x+front+width,y,z+depth,blocktype)
# 
# mc.setBlocks(x+front,y,z,
#              x+front+width,y,z+depth,blocktype)
#===============================================================================

mc.setBlocks(x+front,y,z,\
             x+front+width,y,z+depth,blocktype)