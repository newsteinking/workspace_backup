from mcpi.minecraft import Minecraft
from minecraftstuff import MinecraftDrawing
mc=Minecraft.create()
import time
pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
front=3
blockType=1
radius=5
hight=6
mcdrawing=MinecraftDrawing(mc)
mcdrawing.drawCircle(x+front, y+hight, z+front, radius, blockType)