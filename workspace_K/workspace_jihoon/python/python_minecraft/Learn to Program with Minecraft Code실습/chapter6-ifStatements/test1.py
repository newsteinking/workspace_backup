from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

name=input("What's your name?:")

if name=="{}".format(name):
    mc.postToChat("Your name is {}".format(name))
    
else:
    mc.postToChat("Try again")