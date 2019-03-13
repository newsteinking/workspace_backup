from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time
#===============================================================================
# x,y,z=mc.player.getPos()
#===============================================================================
pos=mc.player.getPos()
x,y,z=pos.x,pos.y,pos.z
front=7
blocktype=0
startx=x
starty=y

CUBE = [[[57, 57, 57, 57], [57, 0, 0, 57], [57, 0, 0, 57], [57, 57, 57, 57]],
        [[57, 0, 0, 57], [0, 0, 0, 0], [0, 0, 0, 0], [57, 0, 0, 57]],
        [[57, 0, 0, 57], [0, 0, 0, 0], [0, 0, 0, 0], [57, 0, 0, 57]],
        [[57, 57, 57, 57], [57, 0, 0, 57], [57, 0, 0, 57], [57, 57, 57, 57]]]
for Cube in CUBE:
    print(Cube)
    for cube1 in reversed(Cube):
        print(cube1)
        for cube2 in cube1:
            print(cube2)
            mc.setBlock(x+front,y,z,cube2)
            time.sleep(0.1)
            x+=1
        y+=1
        x=startx
    z+=1
    y=starty
startx=pos.x   
starty=pos.y

x,y,z=pos.x,pos.y,pos.z
for Cube in CUBE:
    print(Cube)
    for cube1 in Cube:
        print(cube1)
        for cube2 in cube1:
            print(cube2)
            mc.setBlock(x+front+3,y,z,cube2)
            time.sleep(0.1)
            x+=1
        y+=1
        x=startx
    z+=1
    y=starty