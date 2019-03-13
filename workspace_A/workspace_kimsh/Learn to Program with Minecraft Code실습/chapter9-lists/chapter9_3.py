from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

height=[100,0]
count=0
#===============================================================================
# x,y,z=mc.player.getPos()
#===============================================================================
while count<5:
    x,y,z=mc.player.getPos()
    if height[0]<y:
        height[0]=y
    elif height[1]>y:
        height[1]=y
    else:
        print(height)
    mc.postToChat(str(height[0])+","+str(height[1]))
    time.sleep(3)
    count=count+1