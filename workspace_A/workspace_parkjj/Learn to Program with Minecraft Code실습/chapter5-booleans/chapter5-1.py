#-*-coding=cp949
from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time

pos=logan.player.getPos()
x=pos.x
y=pos.y
z=pos.z
#===============================================================================
from random import *
 
i = randint(-128, 128) 
x=i
i = randint(1, 64) 
y=i
i = randint(-128, 128) 
z=i
logan.setBlock(x,y,z,11)

#===============================================================================

#===============================================================================
# try:
#     x=int(input("input your x_number :"))
#     y=int(input("input your y_number :"))
#     print(x/y)  
# except:
#     print("error")
#     
# 
# #logan.postToChat(1/0)
#===============================================================================

pos=logan.player.getPos()
x=pos.x
y=pos.y
z=pos.z
up=3
diamond=57

#logan.setBlock(x+up,y,z,diamond)
block_number=logan.getBlock(x+up,y,z)
logan.postToChat("this block number is {}".format(block_number))
if diamond==block_number:
    logan.postToChat(diamond==block_number)
else:
    logan.postToChat(diamond!=block_number)
    logan.setBlock(x,y-1,z,11)