from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
count=0
while count<5:
    mc.postToChat(count)
    count=count+1
    time.sleep(1)
    mc.postToChat("msg")

mc.postToChat("test")
# for i in range(5):
    # mc.postToChat(i)
    # time.sleep(1)
