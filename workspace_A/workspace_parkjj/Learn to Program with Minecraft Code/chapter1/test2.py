from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x=1
time.sleep(2)
mc.postToChat(x)
my_string="hello, 1"
time.sleep(1)
mc.postToChat(my_string)