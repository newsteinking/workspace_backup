from mcpi.minecraft import Minecraft
import time
import random


def main():
    logan=Minecraft.create()
    count=0
    while count < 16:
        x=random.randrange(-128,128)
        y=random.randrange(0,64)
        z=random.randrange(-128,128)
        logan.player.setPos(x,y,z)
        time.sleep(0.7)
        logan.setBlocks(x-3,y-1,z-3,x+3,y-1,z+3,9)
        count+=1
        
if __name__ == "__main__":
    main()