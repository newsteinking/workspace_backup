from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time

x,y,z=mc.player.getPos()
front=3
def make_block(blockID,acolor):
    if blockID==block.MELON.id:
        mc.setBlock(x+front,y,z,blockID,6)
    
    elif blockID==block.CLAY.id:
        mc.setBlock(x+front+1,y,z,blockID)
        
    elif blockID==block.CHEST.id:
        mc.setBlock(x+front+2,y,z,blockID)
        
    elif blockID==block.ICE.id:
        mc.setBlock(x+front+3,y,z,blockID)
        
    elif blockID==35:
        if acolor=="pink":
            mc.setBlock(x+front,y,z,blockID,6)
            
        elif acolor=="grey":
            mc.setBlock(x+front,y+1,z,blockID,7)
            
        elif acolor=="red":
            mc.setBlock(x+front,y+2,z,blockID,14)
            
        elif acolor=="black":
            mc.setBlock(x+front,y+3,z,blockID,15)
            
        else:
            mc.postToChat("...........")
        
    else:
        mc.postToChat("...sorry...")

while True:       
    block_ID=int(input("input your block number : "))
    acolor=input("input your color name : ")
    make_block(block_ID,acolor)
    
    
    
#===============================================================================
# switch (number)
# {
#  case 1:
#     break;
#  case 2:
#     break;
#  case 3: 
#     break;
#  default:   
#     
# }    
#===============================================================================