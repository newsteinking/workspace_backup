from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
from mcpi import block

blocktype=block.REDSTONE_ORE.id
count=0

while count<30:
    x,y,z=mc.player.getPos()
    count=count+1
    mc.setBlock(x,y-1,z,blocktype)
    time.sleep(0.1)
    mc.postToChat(count)
    
mc.postToChat("finished")


