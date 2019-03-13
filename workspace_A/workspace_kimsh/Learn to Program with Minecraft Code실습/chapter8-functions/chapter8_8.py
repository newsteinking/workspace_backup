from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
import time

def random_block(blocktype,repeatt):
    count=0
    while count<repeatt:
        count+=1
        x1,y1,z1=mc.player.getPos()
        x=random.randrange(int(x1)-20,int(x1)+20)
        y=random.randrange(int(y1),int(y1)+10)
        z=random.randrange(int(z1)-20,int(z1)+20)
        mc.setBlock(x,y,z,blocktype,6)
        mc.player.setPos(x,y+1,z)
        time.sleep(1)
random_block(35,7)