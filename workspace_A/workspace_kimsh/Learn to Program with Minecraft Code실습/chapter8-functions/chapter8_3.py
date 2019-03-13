from mcpi.minecraft import Minecraft
mc=Minecraft.create()

def helloo():
    #===========================================================================
    # mc=Minecraft.create()
    #===========================================================================
    name=input("What's your name? : ")
    mc.postToChat(name)
    
def melon(x,y,z):
    #===========================================================================
    # mc=Minecraft.create()
    #===========================================================================
    blocktype=103
    mc.setBlock(x,y,z,blocktype)
    
#===============================================================================
# for i in range(1,4):
#     helloo()
#===============================================================================

x,y,z=mc.player.getPos()
for i in range(5):
    melon(x+3,y+i,z)
    for j in range(5):
        melon(x+3,y+i,z+j*2)