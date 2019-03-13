from mcpi.minecraft import Minecraft
import time
import random
from mcpi import block

def main():
    logan=Minecraft.create()
    pos=logan.player.getPos()
    x=pos.x
    y=pos.y
    z=pos.z
    tnt=46
    tnt=block.TNT.id
    random_number=random.randint(-128,128)
    for i in range (1,21):
        logan.setBlock(random_number,-1,random_number,tnt)
        time.sleep(0.01)
        blocktype=logan.getBlock(x,y-1,z)
        if blocktype==46:
            logan.setBlock(x,y,z,10)
            time.sleep(2)
            logan.setBlock(x,y,z,0)
            
    logan.postToChat("survive!")
    logan.setBlocks(-128,-1,-128,128,-1,128,24)
    
    
    
    
    
    
    
if __name__=="__main__":
    main()