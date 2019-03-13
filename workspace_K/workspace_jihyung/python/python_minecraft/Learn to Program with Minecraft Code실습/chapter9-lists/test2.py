from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

height=[100,0]

#height[0]
#height[1]

count=0
while count <60:
    x,y,z=mc.player.getPos()
    if y< height[0]:           # y <100
        height[0]=y
    elif y>height[1]:      #y>0
        height[1]=y
        
    count+=1          #count=count+1
    time.sleep(1)
    
mc.postToChat("Lowest:"+str(height[0]))
mc.postToChat("Lowest:{}".format(height[0]))
mc.postToChat("heightest:{}".format(height[1]))
mc.postToChat("height:{}".format(height))