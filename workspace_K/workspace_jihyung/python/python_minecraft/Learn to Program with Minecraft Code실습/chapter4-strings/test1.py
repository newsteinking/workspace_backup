from mcpi.minecraft import Minecraft
sami=Minecraft.create()
sami.postToChat("test")



name=sami.getPlayerEntityIds()
sami.postToChat(name)

pos=sami.player.getPos()
x=pos.x
y=pos.y
z=pos.z
#blocktype=103

blocktype=int(input("input your block number:"))

sami.setBlock(x+2,y,z+2,blocktype)
