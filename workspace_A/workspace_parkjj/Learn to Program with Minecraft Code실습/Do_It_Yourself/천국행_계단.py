from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time

pos=logan.player.getPos()
x=pos.x
y=pos.y
z=pos.z
blocktype=114
up=1
for i in range(0,21):
    logan.setBlocks(x+i,y+i,z-up,x+i,y+i,z+up,blocktype)
    logan.postToChat("{}stairs".format(i))
    time.sleep(0.2)
    