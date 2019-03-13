from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

x=120
y=1
z=-11.5

mc.setBlock(x+2,y,z,0)
mc.setBlock(x+2,y,z+1,0)

blocktype=39
mc.setBlock(x+2,y,z,blocktype)
time.sleep(2)

mc.postToChat("Boom!!")
blocktype=0
mc.setBlock(x+2,y,z,blocktype)

blocktype=5
mc.setBlock(x+2,y,z+1,blocktype)
mc.setBlock(x+2,y,z,blocktype)