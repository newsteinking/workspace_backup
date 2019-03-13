from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
mc=Minecraft.create()


x = 10
y = 11
z = 12
msg='x:{},y:{},z:{}'.format(x,y,z)
mc.postToChat(msg)

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z

msg='x:{},y:{},z:{}'.format(x,y,z)
mc.postToChat(msg)