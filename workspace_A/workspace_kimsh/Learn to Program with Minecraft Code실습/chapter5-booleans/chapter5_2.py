from mcpi.minecraft import Minecraft
bibi=Minecraft.create()
import time

bibi.postToChat("Hello,bibi")
time.sleep(1)

x=-5
y=1
z=6
blocktype=0
bibi.setBlock(x,y,z,blocktype)
time.sleep(1)
blocktype=103
bibi.setBlock(x,y,z,blocktype)
bibi.setting("world_immutable",False)