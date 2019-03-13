from mcpi.minecraft import Minecraft
import time
logan=Minecraft.create()
x,y,z=logan.player.getPos()
logan.setBlocks(x+5,y,z,x+15,
                y+10,z+10,103)

logan.setBlocks(x+5,y,z,x+15,\
                y+10,z+10,103)