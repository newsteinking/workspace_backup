from mcpi.minecraft import Minecraft
mc=Minecraft.create() 
import time

x=-5
y=1
z=6
blocktype=103
mc.setBlock(x,y,z,blocktype)

a=mc.getBlock(x,y,z)
mc.postToChat(a==103)
 
#===============================================================================
# ==
# !=
# <
# <=
# >
# >=
#===============================================================================
time.sleep(1)
b=mc.getBlock(x,y,z)
mc.postToChat(b==0)

time.sleep(1)

NotAir=b !=0
mc.postToChat(NotAir)

time.sleep(1)

if NotAir==0:
    print("I am in air")
    mc.postToChat("I am in air")
else :
    print("I am in ground")
    mc.postToChat("i am in ground")
    
    
    
