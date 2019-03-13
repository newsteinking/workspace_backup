from mcpi.minecraft import Minecraft
import time
logan=Minecraft.create()
#===============================================================================
time.sleep(10)
hits=logan.events.pollBlockHits()
#===============================================================================
print(hits)
for hit in hits:
    x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
    logan.setBlock(x,y,z,11)