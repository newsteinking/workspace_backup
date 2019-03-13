from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

time.sleep(10)
blockhits=mc.events.pollBlockHits()
print(blockhits)
mc.postToChat(len(blockhits))