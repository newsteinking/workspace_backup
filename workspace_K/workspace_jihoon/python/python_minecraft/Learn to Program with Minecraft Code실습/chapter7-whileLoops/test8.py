from mcpi.minecraft import Minecraft 
mc=Minecraft.create()
import time
position=mc.player.getPos()

while True:
    x,y,z=mc.player.getPos()
    ground=mc.getBlock(x,y-1,z)
    if ground!=9:
        mc.setBlock(x,y-1,z,41)
    elif ground==41:
        mc.setBlock(x,y-1,z,)