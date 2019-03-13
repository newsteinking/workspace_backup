from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

a=10
mc.postToChat(a)
time.sleep(1)

if __name__=="__main__":
    a="hello"+"world"
    mc.postToChat(a)
    time.sleep(3)