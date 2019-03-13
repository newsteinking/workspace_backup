from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
blockk=[]
count=0

while count<5:
    x,y,z=mc.player.getPos()
    blocktype=mc.getBlock(x,y,z)
    blockk.append(blocktype)
    time.sleep(1)
    count+=1
if 9 in blockk:
    mc.postToChat("You was in water")
else:
    mc.postToChat("...?")
mc.postToChat("{}".format(blockk))