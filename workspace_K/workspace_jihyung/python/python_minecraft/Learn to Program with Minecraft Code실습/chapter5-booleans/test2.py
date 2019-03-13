from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
mc.postToChat("test")


pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z

#===============================================================================
# blocktype=mc.getBlock(x,y,z)
# mc.postToChat(blocktype)
# bb=blocktype==9
# mc.postToChat(bb)
# if bb:
#     mc.postToChat("your in under water")
#     
# else :
#     mc.postToChat("your in ground")        
#===============================================================================
    
#===============================================================================
# blocktype=block.GOLD_BLOCK.id
# front=2
# mc.setBlock(x+front,y,z,blocktype)
# 
# blockid=mc.getBlock(x+front,y,z)
# mc.postToChat(blockid)
# 
# bb=blockid==blocktype
# mc.postToChat(bb)
# if bb:
#     mc.postToChat("GOLD")
# else:
#     mc.postToChat("No")    
#===============================================================================

x1=-2
z1=16

x2=8
z2=26

bb=x1<x<x2  and z1<z<z2
mc.postToChat(bb)


mc.player.setPos(3,y,21)









