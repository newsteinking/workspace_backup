from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

mc.postToChat("test")

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z

front=3
blocktype=5
btype=True
mc.setBlock(x+front,y,z,blocktype)
mc.setting("world_immutable",btype)
time.sleep(5)
btype=False
mc.setting("world_immutable",btype)




