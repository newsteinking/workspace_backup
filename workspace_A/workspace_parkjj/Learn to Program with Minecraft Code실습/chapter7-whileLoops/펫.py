from mcpi.minecraft import Minecraft
import time
pet=78
bye=9

logan=Minecraft.create()
x,y,z=logan.player.getPos()
logan.setBlock(x-3,y-1,z,bye)
while True:
    logan.setBlock(x,y+3,z,pet)
    x,y,z=logan.player.getPos()
    logan.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,0)
    logan.setBlock(x,y+3,z,pet)
    under_block=logan.getBlock(x,y,z)
    if under_block==9:
        break
    
print("bye!!")