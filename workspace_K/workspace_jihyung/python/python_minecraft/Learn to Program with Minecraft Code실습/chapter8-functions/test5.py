from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

x,y,z=mc.player.getPos()
front=5

def makemelon(x,y,z):
    mc.setBlock(x,y,z,103)
    mc.postToChat("melon created")
    

makemelon(x+front,y,z)
makemelon(x+front,y+1,z)
makemelon(x+front,y,z+1)
makemelon(x+front,y,z-1)