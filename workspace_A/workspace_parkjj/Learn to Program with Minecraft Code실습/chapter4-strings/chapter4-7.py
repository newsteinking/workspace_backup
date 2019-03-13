from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time

pos=logan.player.getPos()
x=pos.x
y=pos.y
z=pos.z
st=1
up=1
ai=0
#===============================================================================
# logan.setBlock(x+up+up,y,z,st)
# time.sleep(0.2)
# logan.setBlock(x+up+up,y,z+up,st)
# time.sleep(0.2)
# logan.setBlock(x+up+up,y,z+up+up,st)
# time.sleep(0.2)
# logan.setBlock(x+up+up,y,z+up+up+up,st)
#===============================================================================

logan.setBlocks(128,1,128,-128,2,-128,ai)
for i in range(3):
    logan.setBlock(x+up+up,y,z+i,st)
    time.sleep(0.2)


choose=input("continue? [O] [X] :")

if choose=="O":
    for i in range(3):
        logan.setBlock(x+up+up,y,z+i,ai)
        time.sleep(0.2)
    for i in range(200):
        logan.setBlock(x+up+up-i,y+up,z,st)
        time.sleep(0.2)
