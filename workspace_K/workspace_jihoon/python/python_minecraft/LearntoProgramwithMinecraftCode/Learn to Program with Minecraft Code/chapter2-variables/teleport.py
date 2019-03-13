#Connect to Minecraft
from mcpi.minecraft import Minecraft
import mcpi.block as block
import time


mc = Minecraft.create()

#Set x, y, and z variables to represent coordinates

x = 100
y = 4
z = -5
"""
x = 0
y = 0
z = 0
"""
#Change the player's position
# mc.player.setTilePos(x, y, z)


time.sleep(5)

mc.setBlock(x,y,z,block.SNOW)

mc2 = Minecraft.create()
mc2.player.setPos(x-5,y,z)

time.sleep(5)
mc2.postToChat("Hello Minecraft world")



