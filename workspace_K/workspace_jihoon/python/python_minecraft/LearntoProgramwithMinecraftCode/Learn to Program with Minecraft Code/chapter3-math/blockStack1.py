from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 145
y = 4
z = -39
blockType = 103
mc.setBlock(x, y, z, blockType)
mc.setBlock(x, y+1, z, blockType)
mc.setBlock(x+2, y , z, blockType)
