from mcpi.minecraft import Minecraft
import time
import random  # random.randint()
#from random import *  randint  random
logan=Minecraft.create()
x,y,z=logan.player.getPos()
while True:
    x+=random.uniform(-0.2,0.2)
    z+=random.uniform(-0.2,0.2)
    y=logan.getHeight(x,z)
    logan.player.setPos(x,y,z)
    time.sleep(0.05)