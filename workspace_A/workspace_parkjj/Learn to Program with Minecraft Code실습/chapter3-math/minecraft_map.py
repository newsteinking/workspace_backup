from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time

#logan.postToChat("test")

pos=logan.player.getPos()

logan.setBlocks(-128,0,-128,128,-64,128,95,5)
logan.setBlocks(-128,0,-128,128,64,128,95,0)

#======================================================
plus=2
real_wood=17
x1=pos.x
y1=pos.y
z1=pos.z
#======================================================