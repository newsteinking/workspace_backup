from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    pos=mc.player.getPos()
    x=pos.x
    y=pos.y
    z=pos.z
    x,y,z=mc.player.getPos()
    #===========================================================================
    # mc.postToChat("x:{},y:{},z:{}".format(x,y,z))
    #===========================================================================
    blocktype=mc.getBlock(x,y,z)
    blocktype2=mc.getBlock(x,y-1,z)
    #===============================================================================
    # mc.postToChat(blocktype)
    #===============================================================================
    if blocktype==9 and blocktype2!=9:
        mc.postToChat("I am under the water.")
        time.sleep(1)