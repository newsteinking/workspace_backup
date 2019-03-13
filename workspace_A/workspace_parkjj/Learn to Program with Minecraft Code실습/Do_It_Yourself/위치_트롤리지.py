#===============================================================================
from mcpi.minecraft import Minecraft
import time
import random
from mcpi import block #block.NAME.id
logan=Minecraft.create()
#===============================================================================
tile_m=1
fence=block.FENCE.id
gold=block.GOLD_BLOCK.id
trap=block.LAVA_STATIONARY.id
grass=2
air=0
#===============================================================================ITEM CODE
time.sleep(3)
x,y,z=logan.player.getPos()
#===============================================================================GET_POS
def making(x,y,z):
    for i in range(1,9):
        logan.setBlock(x,y,z+i,fence)
        time.sleep(0.1)
making(x+4,y,z-4)
def making(x,y,z):
    for i in range(1,9):
        logan.setBlock(x-i,y,z,fence)
        time.sleep(0.1)
making(x+4,y,z+4)
def making(x,y,z):
    for i in range(1,9):
        logan.setBlock(x,y,z-i,fence)
        time.sleep(0.1)
making(x-4,y,z+4)
def making(x,y,z):
    for i in range(1,9):
        logan.setBlock(x+i,y,z,fence)
        time.sleep(0.1)
making(x-4,y,z-4)

logan.setBlocks(x+4,y-1,z+4,x-4,y-1,z-4,tile_m)
logan.player.setPos(x,y,z)
#===============================================================================FENCE/TILE
logan.postToChat("Go to gold block")
time.sleep(2)
logan.postToChat("in three second!")

for j in range(1,3):
    for k in range(1,8):
        r1=random.randrange(-3,3)
        r2=random.randrange(-3,3)
        logan.setBlock(x+r1,y-1,z+r2,gold)                                
        time.sleep(0.1)                    
    time.sleep(3)
     
    x1,y1,z1=logan.player.getPos()
    checking=logan.getBlock(x1,y1-1,z1)                      
    if checking==41:
        logan.player.setPos(x1,y1+2,z1)
        logan.setBlocks(x+3,y-1,z+3,x-3,y-1,z-3,trap)           
        logan.setBlock(x1,y1-1,z1,gold)
        time.sleep(3)
        logan.setBlocks(x+3,y-1,z+3,x-3,y-1,z-3,tile_m)
    else:
        logan.postToChat("game over")                                
        logan.setBlocks(x+5,y-1,z+5,x-5,y-1,z-5,grass)
        logan.setBlocks(x+5,y,z+5,x-5,y,z-5,air)
        time.sleep(500)
        break
#===============================================================================1ROUND
logan.postToChat("2 Round!")
tile_m=35,4
logan.setBlocks(x+4,y-1,z+4,x-4,y-1,z-4,tile_m)

for j in range(1,4):
    for k in range(1,7):
        r1=random.randrange(-3,3)
        r2=random.randrange(-3,3)
        logan.setBlock(x+r1,y-1,z+r2,gold)                                
        time.sleep(0.1)                    
    time.sleep(2.5)
     
    x1,y1,z1=logan.player.getPos()
    checking=logan.getBlock(x1,y1-1,z1)                      
    if checking==41:
        logan.player.setPos(x1,y1+2,z1)
        logan.setBlocks(x+3,y-1,z+3,x-3,y-1,z-3,trap)           
        logan.setBlock(x1,y1-1,z1,gold)
        time.sleep(3)
        logan.setBlocks(x+3,y-1,z+3,x-3,y-1,z-3,tile_m)
    else:
        logan.postToChat("game over")                                
        logan.setBlocks(x+5,y-1,z+5,x-5,y-1,z-5,grass)
        logan.setBlocks(x+5,y,z+5,x-5,y,z-5,air)
        time.sleep(500)
        break
#===============================================================================2ROUND
logan.postToChat("3 Round~! Nice!")
tile_m=block.ICE.id
logan.setBlocks(x+4,y-1,z+4,x-4,y-1,z-4,tile_m)

for j in range(1,6):
    for k in range(1,5):
        r1=random.randrange(-3,3)
        r2=random.randrange(-3,3)
        logan.setBlock(x+r1,y-1,z+r2,gold)                                
        time.sleep(0.1)  
    for k in range(1,3):
        r1=random.randrange(-3,3)
        r2=random.randrange(-3,3) 
        logan.setBlock(x+r1,y,z+r2,fence)                
    time.sleep(2.5)
     
    x1,y1,z1=logan.player.getPos()
    checking=logan.getBlock(x1,y1-1,z1)                      
    if checking==41:
        logan.player.setPos(x1,y1+2,z1)
        logan.setBlocks(x+3,y-1,z+3,x-3,y-1,z-3,trap)           
        logan.setBlock(x1,y1-1,z1,gold)
        time.sleep(3)
        logan.setBlocks(x+3,y-1,z+3,x-3,y-1,z-3,tile_m)
    else:
        logan.postToChat("game over")                                
        logan.setBlocks(x+5,y-1,z+5,x-5,y-1,z-5,grass)
        logan.setBlocks(x+5,y,z+5,x-5,y,z-5,air)
        time.sleep(500)
        break
#===============================================================================3ROUND
logan.postToChat("Thanks 4 playing")
tile_m=35,4
fence=95,4
logan.setBlocks(x+4,y-1,z+4,x-4,y-1,z-4,tile_m)
logan.setBlocks(x+3,y,z+3,x-3,y,z-3,air)

while True:
    for k in range(1,4):
        r1=random.randrange(-3,3)
        r2=random.randrange(-3,3)
        logan.setBlock(x+r1,y-1,z+r2,gold)
        logan.setBlock(x+r1,y+1,z+r2,fence)                               
        time.sleep(0.1)               
    time.sleep(2.5)
     
    x1,y1,z1=logan.player.getPos()
    checking=logan.getBlock(x1,y1-1,z1)                      
    if checking==41:
        logan.player.setPos(x1,y1+2,z1)
        logan.setBlocks(x+3,y-1,z+3,x-3,y-1,z-3,trap)           
        logan.setBlock(x1,y1-1,z1,gold)
        time.sleep(3)
        logan.setBlocks(x+3,y-1,z+3,x-3,y-1,z-3,tile_m)
        logan.setBlocks(x+3,y+1,z+3,x-3,y+1,z-3,air)
    else:
        logan.postToChat("game over")                                
        logan.setBlocks(x+5,y-1,z+5,x-5,y-1,z-5,grass)
        logan.setBlocks(x+5,y,z+5,x-5,y,z-5,air)
        break