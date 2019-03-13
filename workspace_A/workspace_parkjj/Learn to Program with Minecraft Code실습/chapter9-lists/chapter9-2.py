from mcpi.minecraft import Minecraft
import time
logan=Minecraft.create()

height=[100,0]
count=0
while count<60:
    x,y,z=logan.player.getPos()
    
    if y<height[0]:
        height[0]=y
    elif y > height[1]:
        height[1]=y
    time.sleep(0.1)
    count+=1
    
    
logan.postToChat("Low height = {}".format(height[0]))
logan.postToChat("High height = {}".format(height[1]))