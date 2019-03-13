from mcpi.minecraft import Minecraft
import time
yellow=35,4
red=35,14
blue=35,3


def main():
    logan=Minecraft.create()
    x1,y1,z1=logan.player.getPos()
    logan.setBlocks(x1+10,y1-1,z1+10,x1-10,y1-1,z1-10,blue)
    under_block=logan.getBlock(x1,y1-1,z1)
    x2,y2,z2=logan.player.getPos()
    
    while x2-11<x1<x2+11 and z2-11<z1<z2+11:
        logan.setBlocks(x1+10,y1-1,z1+10,x1-10,y1-1,z1-10,blue)
        time.sleep(0.1)
        logan.setBlocks(x1+10,y1-1,z1+10,x1-10,y1-1,z1-10,yellow)
        time.sleep(0.1)
        logan.setBlocks(x1+10,y1-1,z1+10,x1-10,y1-1,z1-10,red)
        time.sleep(0.1)
        x2,y2,z2=logan.player.getPos()
    logan.setBlocks(x1+50,y1-1,z1+50,x1-50,y1-1,z1-50,24)
    
if __name__ == "__main__":
    main()