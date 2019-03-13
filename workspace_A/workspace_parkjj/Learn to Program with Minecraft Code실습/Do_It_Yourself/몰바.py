from mcpi.minecraft import Minecraft
from mcpi import block
import time
import random
logan=Minecraft.create()
x,y,z=logan.player.getPos()
tile_m=1
fence=block.FENCE.id
gold=block.GOLD_BLOCK.id
trap=block.LAVA_STATIONARY.id
grass=2
logan.player.setPos(x,y,z)
count=0.00
point=0
#===============================================================================SETTING
def making(x,y,z):
    for i in range(1,15):
        logan.setBlock(x,y,z+i,fence)
        time.sleep(0.05)
making(x+7,y,z-7)
def making(x,y,z):
    for i in range(1,15):
        logan.setBlock(x-i,y,z,fence)
        time.sleep(0.05)
making(x+7,y,z+7)
def making(x,y,z):
    for i in range(1,15):
        logan.setBlock(x,y,z-i,fence)
        time.sleep(0.05)
making(x-7,y,z+7)
def making(x,y,z):
    for i in range(1,15):
        logan.setBlock(x+i,y,z,fence)
        time.sleep(0.05)
making(x-7,y,z-7)

logan.setBlocks(x+7,y-1,z+7,x-7,y-1,z-7,tile_m)
logan.player.setPos(x,y,z)
#===============================================================================FENCE/TILE
r1=random.randrange(-6,6)
r2=random.randrange(-6,6)
logan.setBlock(x+r1,y-1,z+r2,trap)

r3=random.randrange(-6,6)
r4=random.randrange(-6,6)
logan.setBlock(x+r3,y-1,z+r4,trap)

r5=random.randrange(-6,6)
r6=random.randrange(-6,6)
logan.setBlock(x+r5,y-1,z+r6,trap)

    
while count<=3.00000:
    x0,y0,z0=logan.player.getPos()
    logan.setBlock(x0,y0-1,z0,tile_m)
    logan.setBlock(x0,y0,z0,0)
    time.sleep(0.00001)
    count+=0.00001

a=logan.getBlock(x+r1,y-1,z+r2)
b=logan.getBlock(x+r3,y-1,z+r4)
c=logan.getBlock(x+r5,y-1,z+r6)
#===============================================================================GAME
if a==tile_m and b==tile_m and c==tile_m:
    point=+1
else:
    print("Game Over")
    def making(x,y,z):
        for i in range(1,15):
            logan.setBlock(x,y,z+i,0)
            time.sleep(0.05)
    making(x+7,y,z-7)
    def making(x,y,z):
        for i in range(1,15):
            logan.setBlock(x-i,y,z,0)
            time.sleep(0.05)
    making(x+7,y,z+7)
    def making(x,y,z):
        for i in range(1,15):
            logan.setBlock(x,y,z-i,0)
            time.sleep(0.05)
    making(x-7,y,z+7)
    def making(x,y,z):
        for i in range(1,15):
            logan.setBlock(x+i,y,z,0)
            time.sleep(0.05)
    making(x-7,y,z-7)
    
    logan.setBlocks(x+7,y-1,z+7,x-7,y-1,z-7,grass)
    logan.player.setPos(x,y,z)
    logan.postToChat("You got {} point!".format(point))
#===============================================================================OUT_SETTING





