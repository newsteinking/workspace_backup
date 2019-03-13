from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

ps=mc.player.getPos()
x=ps.x
y=ps.y
z=ps.z
front=3
block_t=56
mc.setBlock(x+front,y,z,block_t)

check_b=mc.getBlock(x+front,y,z)

if check_b==56:
    mc.postToChat("x:{}, y:{}, z:{}".format(x+front,y,z))
    mc.postToChat(str(x+front)+":"+str(y)+":"+str(z)+":")
    
elif check_b==0:
    mc.postToChat("x:{}, y:{}, z:{}".format(x+front,y,z))
    mc.postToChat(str(x+front)+":"+str(y)+":"+str(z)+":")
    
else:
    mc.postToChat("I dont know...")
time.sleep(1)
    
#  C=(F-32)*(5/9)
#  F=C*(5/9)+32    

F=int(input("input your F : "))
C=(F-32)*(5/9)
print(C)