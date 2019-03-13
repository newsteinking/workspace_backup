from mcpi.minecraft import Minecraft
import time
logan=Minecraft.create()
lists=[[1],[2,2],[3,3,3],[4,4,4,4],[5,5,5,5,5]]
x,y,z=logan.player.getPos()
startx=x
starty=y

for list in lists:
    for color in list:
        logan.setBlock(x+3,y,z,35,color)
        y+=1
        time.sleep(0.2)
    z+=1   
    x=startx
    y=starty
    time.sleep(0.2)