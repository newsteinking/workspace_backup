from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 120
y = 4
z = -12

mc.player.setPos(x, z, y)
#mc.player.setTilePos(x, y, z)
