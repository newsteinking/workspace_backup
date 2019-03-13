from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc=Minecraft.create()

def test():
    """
    This is TEST
    
    """
    mc.postToChat("test")
    x,y,z=mc.player.getPos()
    front=5
    blocktype=block.SAND.id
    mc.setBlocks(x+front,y,z,x+front \
                 ,y,z+front,blocktype)
    
if __name__=="__main__":
    test()
    
