from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
mc.postToChat("test")
x=100
y=200
z=x+y
mc.postToChat(z)
time.sleep(1)
z=x-y
mc.postToChat(z)
time.sleep(2)
z=x/y
mc.postToChat(z)
y=3
z=x/y
mc.postToChat(z)
z=x%y
mc.postToChat(z)
z=x//y
mc.postToChat(z)
z=x*y
mc.postToChat(z)
msg="project"
mc.postToChat(msg+"test")














