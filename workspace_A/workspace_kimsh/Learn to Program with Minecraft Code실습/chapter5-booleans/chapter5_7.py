from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

width=10
length=6

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z

x1=x-width
x2=x+width
z1=z-length
z2=z+length

inside=x1<x<x2 and z1<z<z2

#===============================================================================
# mc.postToChat(check)
#===============================================================================

if inside:
    mc.postToChat("inside")
    
else:
    mc.postToChat("outside")
    
### c
#===============================================================================
# void main()
# {
#     if(check ==0)
#     {
#         
#     }
#     else 
#     {
#         
#         
#     }
# 
# }
#===============================================================================

time.sleep(1)

mc.postToChat("test_"+str(inside))