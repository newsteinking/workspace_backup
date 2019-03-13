from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

time.sleep(20)

blockhits=mc.events.pollBlockHits()

print(blockhits)
n=len(blockhits)

mc.postToChat("your score is"+str(n))
