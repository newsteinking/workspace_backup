from mcpi.minecraft import Minecraft
import time

def main():
    logan=Minecraft.create()
    pos=logan.player.getPos()
    x=pos.x
    y=pos.y
    z=pos.z
    
    logan.setBlocks(x+1,y,z-1,x+1,y+2,z+1,11)
    time.sleep(5)
    blocktype=logan.getBlock(x+1,y,z)
    if blocktype!=0:
        logan.postToChat("not air")
        if blocktype == 11:
            logan.postToChat("wall")
            
    else:
        logan.postToChat("air")
        
if __name__ == "__main__":
    main()
    