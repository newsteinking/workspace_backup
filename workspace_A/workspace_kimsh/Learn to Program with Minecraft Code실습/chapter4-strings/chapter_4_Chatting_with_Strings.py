from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

mc.postToChat("\"")

a="hello"
mc.postToChat(a)

time.sleep(1)

msg="hello  {}".format(a)
mc.postToChat(a+str(3))

time.sleep(1)

mc.postToChat(a*3)

time.sleep(1)

mc.postToChat(3**4)