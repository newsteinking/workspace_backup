from mcpi.minecraft import Minecraft
mc=Minecraft.create()

mc.postToChat("test")

check=input("create block?:y or n")

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z


#===============================================================================
# if check =="y":
#     mc.setBlock(x+2,y,z+4,49)
#     mc.postToChat("yes")
#  
# elif check=="yes":
#     mc.postToChat("yes") 
#     
# else:
#     mc.postToChat("no")
#===============================================================================
if check =="y":
    mc.setting("world_immutable",True)
    
