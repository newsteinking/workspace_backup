from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z

mc.setBlock(x+2,y,z,103)

q=input("immutable setting??? : ")
if q=="yes":
    mc.setting("world_immutable",True)
    
else:
    mc.setting("world_immutable",False)