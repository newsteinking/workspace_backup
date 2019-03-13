from mcpi.minecraft import Minecraft
mc=Minecraft.create()

name=input("what your name")

if name=="Sam":
    mc.postToChat("Your name is {}".format(name))
else:
    mc.postToChat("try again")
    
    
    