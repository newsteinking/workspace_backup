from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
count=0
xlist=[]
zlist=[]

while count<5:
    pos=mc.player.getPos()
    xlist.append(pos.x)
    zlist.append(pos.z)
    time.sleep(1)
    count+=1
mc.postToChat("{}".format(xlist))
mc.postToChat("{}".format(zlist))