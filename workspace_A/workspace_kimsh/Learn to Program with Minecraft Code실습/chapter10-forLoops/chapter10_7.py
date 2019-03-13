from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time
x,y,z=mc.player.getPos()
front=3
blocktype=35
count=0

number=int(input("input your colors : "))
colors=[]

for i in range(0,number):
    ainput=int(input("input your color : "))
    colors.append(ainput)
    time.sleep(1)
    
for color in colors:
    mc.setBlock(x+front,y+count,z,blocktype,color)
    count+=1