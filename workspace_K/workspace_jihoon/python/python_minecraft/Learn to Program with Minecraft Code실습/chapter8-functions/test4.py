from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

def getwoolstate(color):
    if color=="pink":
        blockcolor=6
    elif color=="black":
        blockcolor=15
    elif color=="gray":
        blockcolor=7
    return blockcolor
x,y,z=mc.player.getPos()
a=input()
mc.setBlock(x+2,y,z+2,35,getwoolstate(a))
b=input()
mc.setBlock(x+2,y+1,z+2,35,getwoolstate(b))
