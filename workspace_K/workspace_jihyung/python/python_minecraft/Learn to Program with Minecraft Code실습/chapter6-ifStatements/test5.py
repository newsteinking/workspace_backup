from mcpi.minecraft import Minecraft
from minecraftstuff import MinecraftDrawing
from mcpi import block
mc=Minecraft.create()
pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
blockType=block.WATER

mcdrawing=MinecraftDrawing(mc)

mcdrawing.drawCircle(x+6, y+10, z, 3, blockType)