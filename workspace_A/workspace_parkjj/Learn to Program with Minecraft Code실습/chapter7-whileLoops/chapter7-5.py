from mcpi.minecraft import Minecraft
import time

def main():
    logan=Minecraft.create()
    an_input=int(input("Do you want to be an Elsa? [Yes=1]  [No=0]  :"))
    count=1
    while an_input==1 and count<2:
        for i in range(1,100):
            time.sleep(0.01)
            x,y,z=logan.player.getPos()
            logan.setBlock(x,y-1,z,79)
        an_input=int(input("Do you want to be an Elsa one more time? [Yes=1]  [No=0]  :"))
        count+=1
        
        
if __name__=="__main__":
    main()