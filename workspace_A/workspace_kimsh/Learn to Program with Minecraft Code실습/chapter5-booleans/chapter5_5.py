from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
type=mc.getBlock(x,y,z)
up=1
#y+=1
type2=mc.getBlock(x,y+up,z)
water=9

aa=type==9 and type2==0
mc.postToChat(aa)

time.sleep(1)

if aa==True:
    mc.postToChat("I am on water.")
    
else:
    mc.postToChat("I am under the water.")
    
time.sleep(1)
    
bb=type==9 or type2==0
mc.postToChat(bb)