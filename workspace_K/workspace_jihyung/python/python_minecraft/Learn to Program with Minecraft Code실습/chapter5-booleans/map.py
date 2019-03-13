from mcpi.minecraft import Minecraft
mc=Minecraft.create()

from mcpi import block

stone=block.GLASS.id
mc.setBlocks(-128,0,-128,128,64,128,0)
mc.setBlocks(-128,0,-128,128,-64,128,stone)