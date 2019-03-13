from mcpi.minecraft import Minecraft
#===============================================================================
# mc=Minecraft.create()
#===============================================================================
import time

def main():
    mc=Minecraft.create()
    pasw="potato"
    paswinput=input("input your password : ")
    count=0
    while pasw!=paswinput and count<4:
        count+=1
        mc.postToChat(count)
        paswinput=input("input your password one more time : ")
        if pasw==paswinput:
            mc.postToChat("password is true.")
        
        else:
            mc.postToChat("password is false.")
    time.sleep(1)
    mc.postToChat("finish!!")
    
if __name__=="__main__":
    main()