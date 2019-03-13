from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

mc.player.setTilePos(20,4,20)

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

width = 3
height = 3
length = 3
blockType = 4
"""
width = 142
height = 4
length = -40
"""


blockType = 4
air = 0


time.sleep(5)

mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)
# mc.setBlocks(x + 1, y + 1, z + 1,
             # x + width - 1, y + height - 1, z + length - 1, air)
mc.setBlocks(x + 1, y + 1, z + 1,x + width - 2, y + height - 2, z + length - 2, 0)