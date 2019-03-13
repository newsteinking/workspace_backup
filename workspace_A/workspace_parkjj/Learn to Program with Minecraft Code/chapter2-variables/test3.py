from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#Set x, y, and z variables to represent coordinates
x = 63.5
y = 1.0
z = 113.5

#Change the player's position
mc.player.setPos(x, y, z)
