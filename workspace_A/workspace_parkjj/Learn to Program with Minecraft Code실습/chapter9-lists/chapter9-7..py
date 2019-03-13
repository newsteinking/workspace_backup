from mcpi.minecraft import Minecraft
import time
logan=Minecraft.create()

time.sleep(10)

blockhits=logan.events.pollBlockHits()

blocks=len(blockhits)
logan.postToChat("your score is.. {}".format(blocks))
#logan.postToChat("your score is.. {}".format(blockhits))