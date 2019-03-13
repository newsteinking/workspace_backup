from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time


while True:
    x,y,z=logan.player.getPos()
    logan.setBlock(x,y,z,10)
    logan.setBlock(x,y,z,9)