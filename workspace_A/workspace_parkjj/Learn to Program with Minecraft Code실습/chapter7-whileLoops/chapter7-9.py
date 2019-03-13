from mcpi.minecraft import Minecraft
import time
logan=Minecraft.create()

x,y,z=logan.player.getPos()
under_block=logan.getBlock(x,y-1,z)
while not under_block==0:
    logan.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,35,14)
    x,y,z=logan.player.getPos()
    under_block=logan.getBlock(x,y-1,z)
    