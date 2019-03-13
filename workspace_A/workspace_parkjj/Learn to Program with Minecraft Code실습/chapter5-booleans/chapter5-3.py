from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time

pos=logan.player.getPos()
x=pos.x
y=pos.y
z=pos.z

air=0
point=logan.getBlock(x,y-1,z)

bbb=point==air

if bbb==True:
    print("good bye")
    logan.setBlocks(x,1,z,x,-64,z,0)
    logan.setBlock(x,1,z,11)
    logan.player.setPos(x,1,z)
else:
    print("good bye")
    logan.setBlocks(x,-1,z,x,-64,z,0)
    logan.setBlock(x,32,z,11)
    logan.player.setPos(x,32,z)