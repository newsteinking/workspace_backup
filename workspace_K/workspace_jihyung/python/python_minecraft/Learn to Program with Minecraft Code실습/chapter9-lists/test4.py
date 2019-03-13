from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

blocks=[20,56,57,20,56,57,20,56,57]
barblock=22

x,y,z=mc.player.getPos()
starty=y
front=5
count=0
for block in blocks: 
    mc.setBlock(x+front,y,z,block[count])
    y+=1
    count+=1
    time.sleep(1)
    
mc.postToChat("finish")
time.sleep(1)
blocks.insert(2,barblock)

y=starty
x+=front
for block in blocks: 
    mc.setBlock(x+front,y,z,block)
    y+=1
    time.sleep(1)
    
mc.postToChat("finished")