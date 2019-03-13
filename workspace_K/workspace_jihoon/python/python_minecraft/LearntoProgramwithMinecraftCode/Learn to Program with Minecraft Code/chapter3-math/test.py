from mcpi.minecraft import Minecraft 
mc=Minecraft.create()
import time
x=100
y=100
z=3

mc.postToChat(x%z)
mc.postToChat(x-y)
mc.postToChat(y*x)
a="msg"
mc.postToChat(a+str(z))
