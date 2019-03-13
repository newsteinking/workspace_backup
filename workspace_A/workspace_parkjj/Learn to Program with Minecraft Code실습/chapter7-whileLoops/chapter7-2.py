from mcpi.minecraft import Minecraft
import time

def main():
    logan=Minecraft.create()
    count=0
    while count <6 :
        logan.postToChat(count)
        count+=1
        time.sleep(0.5)
    print("finish")   
        
        
if __name__ == "__main__":
    main()