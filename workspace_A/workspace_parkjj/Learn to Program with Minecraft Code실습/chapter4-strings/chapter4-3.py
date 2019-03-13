from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time

pos1=logan.player.getPos()
x1=int(pos1.x)
y1=int(pos1.y)
z1=int(pos1.z)

print(type(x1))

logan.postToChat("You started moving at X={} Y={} Z={}".format(x1,y1,z1))

time.sleep(10)
pos2=logan.player.getPos()
x2=int(pos2.x)
y2=int(pos2.y)
z2=int(pos2.z)
logan.postToChat("You finished moving at X={} Y={} Z={}".format(x2,y2,z2))

xDis=str(x2-x1)
yDis=str(y2-y1)
zDis=str(z2-z1)
time.sleep(3)

print
#logan.postToChat("Distance X={} Y={} Z={}".format(xDis,yDis,zDis))
logan.postToChat("Distance X="+xDis+" Y="+yDis+" Z="+zDis)