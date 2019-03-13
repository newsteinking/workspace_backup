from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()

def snowman():
    x,y,z=mc.player.getPos()
    blocktype=block.SNOW_BLOCK.id
    for i in range(4):
        mc.setBlock(x+1,y+i,z,blocktype)
        
snowman()
    