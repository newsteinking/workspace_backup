from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

a=4
b=109
mc.postToChat(a-b)
print(a-b)
x=90
y=1
z=87
#===============================================================================
# mc.player.setPos(x,y,z)
#===============================================================================
#===============================================================================
# x=66
# y=1
# z=56
#===============================================================================
#===============================================================================
# mc.postToChat(x/y*z)
#===============================================================================
#===============================================================================
# time.sleep(2)
# mc.postToChat(x%y)
# time.sleep(2)
# mc.postToChat(x//y)
# time.sleep(2)
# mc.postToChat(x*z)
#===============================================================================
mc.player.setPos(x,y,z)

pos=mc.player.getPos()

#===============================================================================
# mc.setBlock(pos.x+4,pos.y,pos.z,14)
# y=y+1
# mc.setBlock(pos.x+6,pos.y,pos.z,48)
#===============================================================================
mc.setBlocks(x+2,y+40,z,x+8,y,z,87)

























