from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
import random


count=0

x,y,z=mc.player.getPos()


while count <5:
    x=x+random.randint(-20,20)
    y=y+random.randint(0,20)
    z=z+random.randint(-20,20)
    count=count+1
    mc.postToChat("{},{},{}".format(x,y,z))
    mc.player.setPos(x,y,z)
    time.sleep(1)

    
