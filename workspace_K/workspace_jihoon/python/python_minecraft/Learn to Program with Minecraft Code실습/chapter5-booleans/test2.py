from mcpi.minecraft import Minecraft
from mcpi import block
from inspect import getblock
mc = Minecraft.create()
import time

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
#===============================================================================
# blocktype = mc.getBlock(x,y,z)
#===============================================================================

#===============================================================================
# mc.postToChat(blocktype)
#===============================================================================
#===============================================================================
# bb=blocktype==9
# mc.postToChat(bb)
#===============================================================================

#===============================================================================
# if bb:
#     mc.postToChat("You are in the water")
# else:
#     mc.postToChat("You are on the groud")
#===============================================================================
#===============================================================================
# front=2
# blocktype=block.ICE.id
# 
# mc.setBlock(x+front,y,z+front,blocktype)
# 
# blockid=mc.getBlock(x+front,y,z+front)
# 
# mc.postToChat(blockid)
# 
# bb=blocktype==blockid
# 
# if bb:
#     mc.postToChat("it is ice")
# else :
#     mc.postToChat("it isn't ice")
#     
#===============================================================================

x1=-2
z1=16
x2=8
z2=26

bb=x1<x<x2 and z1<z<z2

mc.postToChat(bb)

mc.player.setPos(3,y,21)

mc.postToChat(type(x))