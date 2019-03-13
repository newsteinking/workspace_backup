from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x,y,z=mc.player.getPos()

floorX=x-2
widthx=4
floorZ=z-2
widthz=4
block=1
ground=y-1
mc.setBlocks(x-2,y-1,z-2,x+2,y-1,z+2,block)

while floorX<=x<=floorX+widthx and floorZ<=z<=floorZ+widthz:
    if block==1:
        block=57
    else :
        block=2
    mc.setBlocks(floorX,ground,floorZ,floorX+widthx,ground,floorZ+widthz,block)

    x,y,z=mc.player.getPos()
    time.sleep(1)

mc.postToChat("finshed")