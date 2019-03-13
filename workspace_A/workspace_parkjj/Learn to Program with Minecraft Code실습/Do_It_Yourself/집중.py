from mcpi.minecraft import Minecraft
import time
import random
from mcpi import block
logan=Minecraft.create()
x1,y1,z1=logan.player.getPos()
x=x1+1
y=y1+1
z=z1
count=0
#===============================================================================SETTING
# realb1=block.LAPIS_LAZULI_BLOCK.id
# realb2=35,11
# fake1=9
# fake2=11
eraser=0

logan.setBlocks(x1+2,y1-1,z1-1,x1-2,y1+2,z1+1,block.LAPIS_LAZULI_BLOCK.id)
logan.setBlocks(x,y+1,z,x1-1,y1,z1,eraser)
logan.setBlock(x,y-1,z,block.LAPIS_LAZULI_BLOCK.id)
logan.setBlock(x,y+1,z,block.LAPIS_LAZULI_BLOCK.id)
#===============================================================================CASE
time.sleep(5)
while True:
    for i in range(1,6):
        time.sleep(0.5)
        r1=random.randrange(1,3)
        if r1==1:
            settingb=block.LAPIS_LAZULI_BLOCK.id
        elif r1==2:
            settingb=35,11
        else:
            settingb=11
            
        logan.setBlock(x,y,z,settingb)
        time_j=random.uniform(0.2,0.4)
        time.sleep(time_j)
        getb=logan.getBlock(x,y,z)
        getb2=logan.getBlock(x+1,y,z)
        tnf=False
        if getb == 9 or getb == 0:
            tnf=True
        
            if tnf == True and getb2 == block.LAPIS_LAZULI_BLOCK.id:
                count+=1
                logan.setBlock(x,y,z,eraser)
            else:
                logan.postToChat("Game over")
                break
        else:
            break
        
    time.sleep(0.3)
    r1=random.randrange(1,3)
    if r1==1:
        settingb=block.LAPIS_LAZULI_BLOCK.id
    elif r1==2:
        settingb=35,11
    else:
        settingb=9
        
    logan.setBlock(x,y,z,settingb)
    time_j=random.uniform(0.2,0.4)
    time.sleep(time_j)
    getb=logan.getBlock(x,y,z)
    getb2=logan.getBlock(x+1,y,z)
    tnf=False
    if getb == 9 or getb == 0:
        tnf=True
    
        if tnf == True and getb2 == block.LAPIS_LAZULI_BLOCK.id:
            count+=1
            logan.setBlock(x,y,z,eraser)
        else:
            logan.postToChat("Game over")
            break
    else:
        break

logan.setBlocks(x1+2,y1-1,z1-1,x1-2,y1+2,z1+1,0)
logan.setBlocks(x,y+1,z,x1-1,y1,z1,eraser)
logan.setBlock(x,y-1,z,0)
logan.setBlock(x,y+1,z,0)
logan.setBlocks(x-10,y-1,z-10,x+10,y-1,z+10,2)
logan.postToChat("You get {}!".format(count))
