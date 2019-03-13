from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

y = y + 10
time.sleep(5)
mc.player.setTilePos(x, y, z)
