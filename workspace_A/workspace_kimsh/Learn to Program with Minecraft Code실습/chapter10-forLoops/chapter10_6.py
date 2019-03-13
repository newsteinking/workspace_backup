from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x,y,z=mc.player.getPos()
front=2

colors=[15,2,5,6,14,4,10,12,11,3,7,9,8,16]
for color in colors:
    mc.setBlock(x+front,y,z+1,35,color-1)
    time.sleep(1)
    y+=1

y=y-len(colors)
x+=5
#colors.reverse()
colors.sort()
for color in colors:
    mc.setBlock(x+front,y,z+1,35,color-1)
    time.sleep(1)
    y+=1