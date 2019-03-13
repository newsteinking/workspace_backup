from mcpi.minecraft import Minecraft
import time
logan=Minecraft.create()

blocks=[]
count=0
while count<11:
    hits=logan.events.pollBlockHits()
    #x,y,z=logan.player.getPos()
    if len(hits)>0:
        hit=hits[0]
        hitX,hitY,hitZ=hit.pos.x,hit.pos.y,hit.pos.z
        block=logan.getBlock(hitX,hitY,hitZ)
        blocklist=[]
        blocklist=hitX,hitY,hitZ,block
        print(blocklist)
        blocks.append(hits)
    
    time.sleep(1)
    count+=1
    
print(blocks)

for i in blocks:
    print(i)
    #x,y,z,block=i 
    #logan.setBlock(x,y,z,103)