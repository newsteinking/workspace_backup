from mcpi.minecraft import Minecraft
mc=Minecraft.create()
mc.postToChat("Re")
x=44
y=53
z=103
mc.postToChat(x)
mc.player.setTilePos(x,y,z)
a=input("prto:")
mc.postToChat(a)