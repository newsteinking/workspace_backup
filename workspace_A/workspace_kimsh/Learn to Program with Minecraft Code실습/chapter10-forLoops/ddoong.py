from mcpi.minecraft import Minecraft
import time
logan=Minecraft.create()
fancy=35,12
import random

def making(x,y,z,input_count):
    # piramid 

    for i in range(1,input_count+1):
    
        logan.setBlocks(x,y+8,z+(i*7),x,y+7,z+(i*7),fancy)
        time.sleep(0.1)
        
        logan.setBlocks(x,y+8,z+(i*7),x,y+7,z+(i*7),0)
        time.sleep(0.1)
        logan.setBlocks(x,y+7,z+(i*7),x,y+5,z+(i*7),fancy)
        time.sleep(0.1)
        
        logan.setBlocks(x,y+7,z+(i*7),x,y+5,z+(i*7),0)
        logan.setBlocks(x,y+3,z+(i*7),x,y+4,z+(i*7),fancy)
        time.sleep(0.1)
        
        
        logan.setBlocks(x,y+3,z+(i*7),x,y+4,z+(i*7),fancy)
        logan.setBlocks(x-2,y,z-2+(i*7),x+2,y,z+2+(i*7),fancy)
        logan.setBlocks(x-1,y+1,z-1+(i*7),x+1,y+1,z+1+(i*7),fancy)
        logan.setBlocks(x,y+2,z+(i*7),x,y+3,z+(i*7),fancy)
        time.sleep(0.1)
        
        logan.setBlocks(x,y+2,z+(i*7),x,y+4,z+(i*7),0)
        logan.setBlocks(x-3,y-1,z-2+(i*7),x+2,y-1,z+4+(i*7),fancy)
        logan.setBlocks(x-2,y,z-2+(i*7),x+2,y,z+2+(i*7),fancy)
        logan.setBlocks(x-1,y+1,z-1+(i*7),x+1,y+1,z+1+(i*7),fancy)
        time.sleep(0.1)
        
        logan.setBlocks(x-3,y-1,z-2+(i*7),x+2,y-1,z+4+(i*7),fancy)
        logan.setBlocks(x-2,y,z-2+(i*7),x+2,y,z+2+(i*7),fancy)
        logan.setBlocks(x-1,y+1,z-1+(i*7),x+1,y+1,z+1+(i*7),0)
        time.sleep(0.1)
        
        logan.setBlocks(x-3,y-1,z-2+(i*7),x+2,y-1,z+4+(i*7),fancy)
        logan.setBlocks(x-2,y,z-2+(i*7),x+2,y,z+2+(i*7),0)
        time.sleep(5)
        
        logan.setBlocks(x-3,y-1,z-2+(i*7),x+2,y-1,z+4+(i*7),3)
        time.sleep(5)
        
        logan.setBlocks(x-3,y-1,z-2+(i*7),x+2,y-1,z+4+(i*7),2)
    
    for j in range(1,4):
        rd1=random.randrange(-7,7)
        rd2=random.randrange(-7,7)
        time.sleep(0.05)
        logan.setBlock(x+rd2,y,z+rd1+(i*7),39)
    
    for k in range(1,4):
        rd1=random.randrange(-7,7)
        rd2=random.randrange(-7,7)
        time.sleep(0.05)
        logan.setBlock(x+rd2,y,z+rd1+(i*7),59)
    
    for l in range(1,4):
        rd1=random.randrange(-7,7)
        rd2=random.randrange(-7,7)
        time.sleep(0.05)
        logan.setBlock(x+rd1,y,z+rd2+(i*7),6)

count_input=int(input("how many cuty blocks do you want? :"))
x,y,z=logan.player.getPos()
making(x+5,y,z,count_input,)