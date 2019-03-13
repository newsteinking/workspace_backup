from mcpi.minecraft import Minecraft
import time
from mcpi.block import AIR

def main():
    logan=Minecraft.create()
    
    pos=logan.player.getPos()
    x=pos.x
    y=pos.y
    z=pos.z
    ice=79
    snow=80
    air=0
    lava=11
    up=2
    
    logan.setBlock(x+up,y,z,ice)
    logan.postToChat("Successful making")
    time.sleep(1)
    pos2=logan.player.getPos()
    x=pos2.x
    y=pos2.y
    z=pos2.z
    
    blocktype=logan.getBlock(x+up,y,z)
    
    if blocktype==air:
        logan.postToChat("I lost my cuty ice!! TT")
    elif blocktype==ice:
        logan.postToChat(":D")
    else:
        logan.setBlocks(x-5,y-1,z-5,x+5,y-1,z+5,snow)
        
if __name__=="__main__":
    main()
    
    
    