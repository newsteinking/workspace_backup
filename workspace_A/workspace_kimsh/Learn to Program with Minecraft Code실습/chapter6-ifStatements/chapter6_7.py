from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from mcpi import block
import time

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
front=5
H=4
L=6
W=4
blocktype=block.WOOD.id

#===============================================================================
# mc.setBlocks(x+front,y,z,x+front+L,y+H,z+W,blocktype)
# blocktype=57
# mc.setBlocks(x+front+2,y,z,x+front+L-2,y,z,blocktype)
# mc.setBlocks(x+front+2,y,z,x+front+L-2,y+1,z,blocktype)
#===============================================================================

mc.setBlocks(x+front,y,z,x+front+L,y+H,z+W,blocktype)

blocktype=57
mc.setBlocks(x+front,y,z+2,x+front+L,y+H,z+W-2,blocktype)
