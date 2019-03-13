from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

x,y,z=mc.player.getPos()

def growTree(x,y,z):
    wood=17
    leaves=18
    
    #body
    mc.setBlocks(x,y,z,x,y+5,z,wood)
    
    #leaves
    mc.setBlocks(x-2,y+6,z-2,x+2,y+6,z+2,leaves)
    
    mc.setBlocks(x-1,y+7,z-1,x+1,y+7,z+1,leaves)
#===============================================================================
#     
# growTree(x+10,y,z)   
# growTree(x+20,y,z)   
# growTree(x+30,y,z)   
#===============================================================================
for i in range(1,6):
    growTree(x+10*i,y,z)