from mcpi.minecraft import Minecraft
from minecraftstuff import MinecraftDrawing
logan=Minecraft.create()

pos=logan.player.getPos()
loganDrawing=MinecraftDrawing(logan)
loganDrawing.drawCircle(pos.x, pos.y+20, pos.z, 9, 11)