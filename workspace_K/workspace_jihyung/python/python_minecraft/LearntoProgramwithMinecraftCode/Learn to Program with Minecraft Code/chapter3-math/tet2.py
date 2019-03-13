from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x=4
y=1
z=15
mc.player.setPos(x,y,z)
time.sleep(2)
x=3
y=60
z=90
mc.player.setPos(x,y,z)
time.sleep(2)
x=4
y=1
z=15
mc.player.setPos(x,y,z)
mc.setBlock(x+2,y,z,103)
time.sleep(2)
#===============================================================================
# mc.setBlock(x+2,y,z,0)
#===============================================================================
mc.setBlock(x+2,y,z+1,53)
time.sleep(2)
mc.setBlock(x+2,y,z+2,89)
time.sleep(2)