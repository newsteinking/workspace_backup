from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time
x,y,z=mc.player.getPos()
front=3
blocktype=35

#===============================================================================
# alist=[2,3,5]
#===============================================================================
blist=[[0,0,0],[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]]
print(blist)
for B in blist:
    print(B)
    for b in B:
        print(b)
        mc.setBlock(x,y,z+front,blocktype,b)
        time.sleep(0.5)
        y+=1
    