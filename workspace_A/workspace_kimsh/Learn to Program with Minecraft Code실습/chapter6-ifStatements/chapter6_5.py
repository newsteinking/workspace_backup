from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

mc.player.setPos(1,1,1)
q=int(input("input your number : "))
if 1<q<5:
    mc.player.setPos(1+q,1,1)
    
elif 5<q<10:
    mc.player.setPos(1,1,1+q)
    
elif 10<q<15:
    mc.player.setPos(1,1+q,1)
    
else:
    mc.postToChat("wow wow wow wow...")