from mcpi.minecraft import Minecraft
from minecraftstuff import MinecraftDrawing
from mcpi import block
mc=Minecraft.create()
import time

x,y,z=mc.player.getPos()
mcdrawing=MinecraftDrawing(mc)
mcdrawing.drawCircle(x,y+5,z,5,block.BEDROCK.id)