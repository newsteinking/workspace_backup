from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from mcpi import block

mc.setBlocks(-128,0,-128,128,64,128,0)
blockID=block.GRASS.id
mc.setBlocks(-128,0,-128,128,-64,128,blockID)