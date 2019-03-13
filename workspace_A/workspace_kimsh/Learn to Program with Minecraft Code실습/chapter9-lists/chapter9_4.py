from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time

x,y,z=mc.player.getPos()
blockk=[block.NETHER_REACTOR_CORE.id,block.DIAMOND_ORE.id,block.LAPIS_LAZULI_ORE.id]
barblock=22
count=0
front=3
while count<=len(blockk):
    for i in range(len(blockk)):
        mc.setBlock(x,y,z+front+count*count,blockk[i])
        time.sleep(1)
        count+=1
    #===========================================================================
    # mc.setBlock(x+front+count,y+count,z,blockk[0])
    # time.sleep(1)
    # mc.setBlock(x+front+1+count,y+count,z,blockk[1])
    # time.sleep(1)
    # mc.setBlock(x+front+2+count,y+count,z,blockk[2])
    # time.sleep(2)
    # count+=1
    # del blockk[1]
    # #blockk[1]=barblock
    # blockk.insert(1,barblock)
    # time.sleep(1)
    #===========================================================================