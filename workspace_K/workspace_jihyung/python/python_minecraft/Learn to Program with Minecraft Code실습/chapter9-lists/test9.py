from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
import random


blocks=[56,67,42,54,98]

#block=ramdom.choice(blocks)

x,y,z=mc.player.getPos()
starty=y
#===============================================================================
# for i in range(6):
#     block=random.choice(blocks)
#     mc.setBlock(x+5,y+i,z+2,block)
#  
#===============================================================================
for block in blocks:
    mc.setBlock(x+10,y,z,block)
    y+=1


y=starty
for count,block in enumerate(blocks):
    mc.setBlock(x+3,y+count,z,block) 
    
    
for ablock in enumerate(blocks):
    print(ablock)
    #mc.setBlock(x+3,y+count,z+10,block)    
   
#===============================================================================
# count=0 
# while cout <6:
#     
#     cout+=1
#     
#===============================================================================
