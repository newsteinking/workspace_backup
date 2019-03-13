from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

x,y,z=mc.player.getPos()
front=2
up=1

def getwoolstate(color):
    if color=="pink":
        blockcolor=6
    elif color=="black":
        blockcolor=15
    elif color=="gray":
        blockcolor=7
    return blockcolor
mc.setBlock(x+front,y,z+front,35,getwoolstate("gray"))
