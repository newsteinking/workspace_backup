
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

#===============================================================================
# pos=mc.player.getPos()
# 
# x=pos.x
# y=pos.y
# z=pos.z
# 
# 
# x2=10
# y2=1
# z2=10
# xdis=x2-x
# ydis=y2-y
# zdis=z2-z
# dis="x:{} Y:{} Z:{}".format(xdis,ydis,zdis)
# mc.postToChat(dis)
# 
# mc.postToChat(str(xdis)+":"+str(ydis)+":"+str(zdis))
#===============================================================================
name=input("input your name:")
msg=input("input your msg:")
mc.postToChat(name+":"+msg)














