from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
count=0

pos=mc.player.getPos()
xlist=[]
zlist=[]
xlist.append(pos.x)
zlist.append(pos.z)
time.sleep(3)

pos2=mc.player.getPos()
xlist.append(pos2.x)
zlist.append(pos2.z)

mc.postToChat("{}".format(xlist))
mc.postToChat("{}".format(zlist))