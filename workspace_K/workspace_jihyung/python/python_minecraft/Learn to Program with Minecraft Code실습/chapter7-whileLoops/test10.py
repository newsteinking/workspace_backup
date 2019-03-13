from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

air=0
water=9
blocktype=41
while True:
    x,y,z=mc.player.getPos()
    groundblock=mc.getBlock(x,y-1,z)
    
    #===========================================================================
    # if groundblock !=air and groundblock !=water:
    #===========================================================================
    if groundblock !=water:
        mc.setBlock(x,y-1,z,blocktype)