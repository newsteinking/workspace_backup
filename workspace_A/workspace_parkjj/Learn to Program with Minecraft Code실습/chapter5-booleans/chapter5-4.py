from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time
import math

pos1=logan.player.getPos()
x1=pos1.x
z1=pos1.z
y1=pos1.y

logan.postToChat("start timer(5s)")
while True:
    pos0=logan.player.getPos()
    x=pos0.x
    y=pos0.y
    z=pos0.z
    logan.setBlock(x,y,z,2)
    
    time.sleep(5)
    
    pos2=logan.player.getPos()
    x2=pos2.x
    z2=pos2.z
    y2=pos2.y
    distance_xy=int(math.sqrt((x2-x1)**2+(z2-z1)**2))
    distance_xyz=int(math.sqrt((distance_xy)**2+(y2-y1)**2))
    if distance_xyz>=15:
        logan.postToChat("You are so fast! You moved around {}".format(distance_xyz))
    else:
        logan.postToChat("Are you turtle? HaHa. You moved around {}".format(distance_xyz))
    
    time.sleep(4)
    logan.postToChat("10s Free time")
    time.sleep(10)
        
