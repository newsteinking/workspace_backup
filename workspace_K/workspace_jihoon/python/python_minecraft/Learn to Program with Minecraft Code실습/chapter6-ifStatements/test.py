from mcpi.minecraft import Minecraft 
from tkinter.constants import YES
mc=Minecraft.create()
import time

pos=mc.player.getPos()
x=pos.x+2
y=pos.y
z=pos.z
blocktype=1

check=input("Create block? or not?:")

#===============================================================================
# if check=="yes":
#     mc.setBlock(x,y,z,blocktype)
# 
# elif check=="Umm..":
#     mc.postToChat("You have to think more")
#     
# else :
#    mc.postToChat("No")
#    
#===============================================================================
#===============================================================================
# if check == "y":
#     mc.setting("world_immutable",True)
# else:
#     mc.setting("world_immutable",False)
#===============================================================================