from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time


if __name__== "__main__" :
    a="hallow"+'world'
    time.sleep(2)
    mc.postToChat(a)
