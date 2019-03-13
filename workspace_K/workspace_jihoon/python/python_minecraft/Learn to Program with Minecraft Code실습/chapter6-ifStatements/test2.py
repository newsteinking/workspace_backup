from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
front=5
blocktype=2
#===============================================================================
# blocktype=int(input("blocktype:"))
# createblock=input("Create block? Yes or No:")
# if createblock=="Yes":
#     mc.setBlock(x+front,y,z,blocktype)
#===============================================================================
mc.setBlock(x+front,y,z,blocktype)

blocknumber=mc.getBlock(x+front,y,z)
if blocknumber=="2":
    mc.postToChat("Your blocktype is {}".format(blocktype))
else:
    print("test")
