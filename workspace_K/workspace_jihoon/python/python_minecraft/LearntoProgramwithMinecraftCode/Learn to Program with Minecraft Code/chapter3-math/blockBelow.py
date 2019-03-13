from mcpi.minecraft import Minecraft
import time


mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
blockType = 10

y = y - 1

time.sleep(5)

mc.setBlock(x, y, z, blockType)
