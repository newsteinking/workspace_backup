from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
 
x,y,z=mc.player.getPos()
position=1
while 0<position<10:
    x,y,z=mc.player.getPos()
    position=int(input("input your 'x' number:")) 
    mc.player.setPos(x+position,y,z)
    mc.postToChat("{},{},{}".format(int(x),int(y),int(z)))
    time.sleep(1)

mc.postToChat("finished")