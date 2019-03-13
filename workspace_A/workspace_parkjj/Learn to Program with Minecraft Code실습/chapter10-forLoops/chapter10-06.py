from mcpi.minecraft import Minecraft
import time
import random
logan=Minecraft.create()

def brokenblock():
    brokenblocks=[48,67,4,4,4,4]
    block=random.choice(brokenblocks)
    return block
x,y,z=logan.player.getPos()
brokenwalls=[]
height=5
witdh=10
startx=x
for i in range(height):
    brokenwalls.append([])
    for j in range(witdh):
        block=brokenblock()
        brokenwalls[i].append(block)
        
print(brokenwalls)
for wall in brokenwalls:
    for block in wall:
        logan.setBlock(x+3,y,z,block)
        x+=1
    y+=1
    x=startx
    