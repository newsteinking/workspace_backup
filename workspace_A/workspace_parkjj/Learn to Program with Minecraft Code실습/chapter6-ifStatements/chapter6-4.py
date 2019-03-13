from mcpi.minecraft import Minecraft
import time
import random

def main():
     while True:
        logan=Minecraft.create()
        jumping=int(input("How many blocks do you want to jump? [01-05 / 06-10 / 11-15] :"))
        pos=logan.player.getPos()
        x=pos.x
        y=pos.y
        z=pos.z
        
        logan.player.setPos(1,4,1)
        time.sleep(5)
        if 0<jumping<6:
            a=random.randint(1,5)
            logan.player.setPos(x+a,y,z)
            logan.postToChat("You moved {} blocks.".format(a))
            pos=logan.player.getPos()
            x=pos.x
            y=pos.y
            z=pos.z
            logan.setBlocks(x-100,y-10,z-100,x+100,y+10,z+100,0)
            
        elif 5<jumping<11:
            a=random.randint(6,10)
            logan.player.setPos(x+a,y,z)
            logan.postToChat("You moved {} blocks.".format(a))
        
        elif 10<jumping<16:
            a=random.randint(11,15)
            logan.player.setPos(x+a,y,z)
            logan.postToChat("You moved {} blocks.".format(a))
            
        elif 15<jumping:
            logan.postToChat("error")
            
if __name__=="__main__":
    main()