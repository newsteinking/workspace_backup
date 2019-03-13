from mcpi.minecraft import Minecraft
import time
logan=Minecraft.create()
count=0
blocks=[5,39,103,79,80,2,41,30,24,35]
blocks.sort()
x,y,z=logan.player.getPos()
x+=3
a=len(blocks)
while True:
    for i in range(a):
        logan.setBlock(x,y+i,z,blocks[i])
        time.sleep(0.2)
        
    count+=1
    if count==10:
        break
    