from mcpi.minecraft import Minecraft
bibi=Minecraft.create()
import time

pos=bibi.player.getPos()
x=pos.x
y=pos.y
z=pos.z
front=3
blocktype=0

bibi.setBlock(x+front,y,z,blocktype)

check_b=bibi.getBlock(x+front,y,z)
bibi.postToChat(check_b)
time.sleep(1)

if check_b==56:
    bibi.postToChat("your block type is 56.")
    
elif check_b==103:
    bibi.postToChat("your block type is 103.")
    
else:
    bibi.postToChat("I don't know...")    