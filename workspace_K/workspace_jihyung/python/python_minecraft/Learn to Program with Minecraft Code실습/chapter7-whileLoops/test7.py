from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

x,y,z=mc.player.getPos()

position=5

while 0< position <10:
    x,y,z=mc.player.getPos()
    position=int(input("x number"))
    time.sleep(1)
    mc.player.setPos(x+position,y,z)
    mc.postToChat("{},{},{}".format(int(x)+position,int(y),int(z)))

mc.postToChat("finish")