from mcpi.minecraft import Minecraft
from test.test_itertools import take
from random import random
from mcpi import block
mc=Minecraft.create()
import time
import random

a =random.randint(3,23)
blocktype=block.GRASS.id
#===============================================================================
# while I am sleep: 
#     if call:
#         take
#===============================================================================
count=1
mc.setBlocks(-128,0,-128,128,4,128,blocktype)
time.sleep(5)
#===============================================================================
# while count<5:
#===============================================================================
while True:
    mc.postToChat(count)
    x=random.randint(0,50)
    y=random.randint(4,10)
    z=random.randint(0,50)
    mc.postToChat("x : {}, y : {}, z : {}".format(x,y,z))
    mc.player.setPos(x,y,z)
    time.sleep(2)
    mc.setBlock(x,y,z,blocktype)
    put=input("O or X? : ")
    if put=="O":
        mc.postToChat("gogogo!!!")
          
    else:
        break
     
    #===========================================================================
    # count=count+1
    #===========================================================================
    count+=1