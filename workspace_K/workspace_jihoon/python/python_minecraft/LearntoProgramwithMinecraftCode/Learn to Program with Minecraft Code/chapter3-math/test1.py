from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

x=4
y=1
z=15
blocktype=103
mc.player.setPos(x,y,z)
position=mc.player.getPos()

x1=position.x
y1=position.y
z1=position.z

msg="x:{} y:{} z:{}".format(x1,y1,z1)

mc.postToChat(msg)


mc.setBlock(x+2,y,z,blocktype)
mc.setBlock(x+2,y,z+1,blocktype)
mc.setBlock(x+2,y,z+2,blocktype)
mc.setBlock(x+2,y,z+3,blocktype)
mc.setBlock(x+2,y,z+4,blocktype)

time.sleep(2)
blocktype=0

mc.setBlock(x+2,y,z,blocktype)
mc.setBlock(x+2,y,z+1,blocktype)
mc.setBlock(x+2,y,z+2,blocktype)
mc.setBlock(x+2,y,z+3,blocktype)
mc.setBlock(x+2,y,z+4,blocktype)