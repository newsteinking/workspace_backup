from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time

while True:
    pos=logan.player.getPos()
    x=pos.x
    y=pos.y
    z=pos.z
    logan.setBlock(x,y-1,z,103)