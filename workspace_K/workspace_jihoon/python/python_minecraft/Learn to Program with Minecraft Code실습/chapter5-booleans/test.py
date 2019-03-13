from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

front=3
blocktype=103
pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
hight=mc.getHeight(x,z)
mc.postToChat(hight)
mc.setBlock(x+front,y,z,blocktype)
mc.setting("world_immutable", False)
aboveGround = y != hight
mc.postToChat(aboveGround)

for i in range(5):
    mc.setBlock(x+front,y,z+i,blocktype)
