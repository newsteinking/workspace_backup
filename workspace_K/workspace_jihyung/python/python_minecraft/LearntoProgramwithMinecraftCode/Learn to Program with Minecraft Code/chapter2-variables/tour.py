#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

#Set x, y, and z variables to represent coordinates
x = 100
y = 4
z = -5

#Change the player's position
mc.player.setTilePos(x, y, z)

#Wait 10 seconds
time.sleep(10)

#Set x, y, and z variables to represent coordinates
x = 50
y = 4
z = 144

#Change the player's position
mc.player.setTilePos(x, y, z)
