from mcpi.minecraft import Minecraft
tane = Minecraft.create()
import time

tane.postToChat("\*-*/ yee")
pos=tane.player.getPos()
#blocktype=17
#===============================================================================
# blocktype=int(input("input your block:"))
# tane.setBlocks(pos.x,pos.y,pos.z+3,pos.x,pos.y+4,pos.z+3,blocktype)
#===============================================================================

name=tane.getPlayerEntityIds()
tane.postToChat(name)

