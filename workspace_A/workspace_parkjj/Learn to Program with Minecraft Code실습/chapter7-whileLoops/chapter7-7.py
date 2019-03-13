from mcpi.minecraft import Minecraft
import time

def main():
    logan=Minecraft.create()
    count=1
    
    while 0<count<11:
        count=int(input("How many blocks do you want to jump? [1-10] :"))
        x,y,z=logan.player.getPos()
        if not (0<count<10):
            break
        for i in range(1,count+1):
            time.sleep(0.05)
            logan.player.setPos(x+i,y,z)
            print(i)
            
        
    print("Error... ({}) ".format(count))
    
if __name__ == "__main__":
    main()