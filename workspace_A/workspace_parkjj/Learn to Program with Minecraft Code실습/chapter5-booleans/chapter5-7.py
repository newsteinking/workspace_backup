from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time

pos=logan.player.getPos()
x=pos.x
y=pos.y
z=pos.z
length=20
down=2
blocktype=11

logan.setBlocks(x-length,y-down,z-length,x+length,y-down,z+length,blocktype)
time.sleep(5)
check= x-length<x<x+length and z-length<z<z+length
if check==True:
    blocktype=0
    down=1
    logan.setBlocks(x-length,y-down,z-length,x+length,y-down,z+length,blocktype)
    time.sleep(5)
    blocktype=2
    logan.setBlocks(x-length,y-down-down,z-length,x+length,y-down,z+length,blocktype)
    time.sleep(1)
    logan.player.setPos(x,y+5,z)
else:
    logan.postToChat("Welcome surviver!")
#logan.getBlock()