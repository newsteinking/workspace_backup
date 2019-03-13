from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
mc.player.setTilePos(100,4,20)
import random

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
time.sleep(5)

x += random.randrange(-10, 11)
y += random.randrange(0, 11)
z += random.randrange(-10, 11)
mc.player.setPos(x, y, z)
