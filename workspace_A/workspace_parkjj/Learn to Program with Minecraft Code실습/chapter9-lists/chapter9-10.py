from mcpi.minecraft import Minecraft
import time
logan=Minecraft.create()
x,y,z=logan.player.getPos()
colors=[0,1,2,3,4,5]

for color in colors:
    logan.setBlock(x+3,y,z,35,color)
    time.sleep(0.1)
    y+=1
    