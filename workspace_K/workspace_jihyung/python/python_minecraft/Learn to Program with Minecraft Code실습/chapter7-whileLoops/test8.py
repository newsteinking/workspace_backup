from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

x,y,z=mc.player.getPos()
floorx=x-2
floory=y-1
floorz=z-2
width=4
blocktype=41
mc.setBlocks(floorx,floory,floorz,floorx+width,floory,floorz+width,blocktype)


while floorx <= x <=floorx+width and floorz <= z <=floorz+width:
    time.sleep(0.5)
    if blocktype ==41:
        blocktype =57
    else:
        blocktype=41
    
    mc.setBlocks(floorx,floory,floorz,floorx+width,floory,floorz+width,blocktype)
    x,y,z=mc.player.getPos()
    time.sleep(0.5)
    
mc.postToChat("finish")
