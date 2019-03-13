from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
import random

x,y,z=mc.player.getPos()

# pos=mc.player.getPos()
# x,y,z=pos.x,pos.y,pos.z

count=0
while count<5:
    
    x=x+random.randint(-2,2)
    y=y+random.randint(0,5)
    z=z+random.randint(-2,2)
    mc.postToChat("{},{},{}".format(x,y,z))
    mc.player.setPos(x,y,z)
    print(count)
    count=count+1 
    time.sleep(1)
    