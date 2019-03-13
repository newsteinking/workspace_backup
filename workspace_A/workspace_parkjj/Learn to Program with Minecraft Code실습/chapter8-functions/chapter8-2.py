from mcpi.minecraft import Minecraft
import time
logan=Minecraft.create()

def hello(name):
    #logan.postToChat("nice to meet you, {}!".format(name))
    return name 


a=hello(2)
print(a)
print(hello(2))