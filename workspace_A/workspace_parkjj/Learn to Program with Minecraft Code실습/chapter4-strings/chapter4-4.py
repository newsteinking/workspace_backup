from mcpi.minecraft import Minecraft
logan=Minecraft.create()

pos=logan.player.getPos()
x=pos.x
y=pos.y
z=pos.z
GG="GoodGame"
logan.postToChat(type(GG))