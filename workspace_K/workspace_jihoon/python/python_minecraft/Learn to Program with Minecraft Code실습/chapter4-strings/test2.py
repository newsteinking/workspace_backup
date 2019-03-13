from mcpi.minecraft import Minecraft
tane = Minecraft.create()
import time

#===============================================================================
# pos = tane.player.getPos()
# x=pos.x
# y=pos.y
# z=pos.z
# 
# x2=1
# y2=1
# z2=5
# 
# xdis=x2-x
# ydis=y2-y
# zdis=z2-z
# 
# dis="x:{} y:{} z:{}".format(xdis,ydis,zdis)
# tane.postToChat(dis)
#===============================================================================

#===============================================================================
# name = input("What's your name???:")
# msg = input("your msg:")
# 
# tane.postToChat(name+":s"+msg)
#===============================================================================

pos=tane.player.getPos()

tane.setBlocks(pos.x,pos.y,pos.z+3,pos.x,pos.y+3,pos.z+3,17)