from mcpi.minecraft import Minecraft
from wheel.cli.convert import egg2wheel
mc=Minecraft.create()
name="kkkkk"

mc.postToChat(name)


pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
mc.postToChat("x:{},y:{},z:{}".format(x,y,z))

a="egg"
mc.postToChat(a+str(10))

b="x:{},y:{},z:{}".format(x,y,z)
mc.postToChat(b)

blocktype=int(input("input your nuember:"))
mc.setBlock(x+2,y,z+2,blocktype)









