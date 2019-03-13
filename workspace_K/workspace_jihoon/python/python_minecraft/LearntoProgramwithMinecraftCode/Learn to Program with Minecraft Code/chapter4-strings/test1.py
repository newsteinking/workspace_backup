from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

mc.postToChat("minecraft")
pos = mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
#===============================================================================
# mc.postToChat("x:{},y:{},z:{}".format(x,y,z))
#===============================================================================
r="egg"
b="x:{},y:{},z:{}".format(x,y,z)
mc.postToChat(b)
blocktype=int(input("number:"))
mc.setBlock(x+1,y,z,blocktype)

