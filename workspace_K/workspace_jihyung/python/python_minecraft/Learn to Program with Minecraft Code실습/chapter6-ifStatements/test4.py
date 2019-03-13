from mcpi.minecraft import Minecraft
mc=Minecraft.create()

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
front=2
blocktype=103
#===============================================================================
# checkblock=input("create block?Y or N:")
# if checkblock=="Y":
#     mc.setBlock(x+front,y,z+front,blocktype)
# else:
#     mc.postToChat("no")
#===============================================================================

blo=mc.getBlock(x+front,y,z+front)

if blo==103:
    mc.postToChat("your block is {}".format(blo))
else:
    mc.postToChat("No")
    