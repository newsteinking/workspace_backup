from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
import random
count=0

def randomBlock():
    blocklist=[103,35,22,56]
    block=random.choice(blocklist)
    return block
    

history=[]
while count<10:
    pos=mc.player.getPos()
    x,y,z=pos.x,pos.y,pos.z
    postuple=int(x),int(y),int(z),randomBlock()
    #print(postuple)  # (2,3,4,103)
    poslist=list(postuple)
    print(poslist)   #[2,3,4,103]
    history.append(poslist)
    mc.setBlock(x,y,z,randomBlock())
    time.sleep(1.5)
    count+=1
    
mc.postToChat(history)
print(history)
history.sort()
print(history)
history[0][0]
startx=history[len(history)-len(history)][0]
endx=history[len(history)-1][0]
starty=history[len(history)-len(history)][1]
endy=history[len(history)-1][1]
startz=history[len(history)-len(history)][2]
endz=history[len(history)-1][2]
#mc.setBlocks(startx,starty,startz,endx,endy,endz,randomBlock())

Xrange=abs(startx-endx)
Yrange=abs(starty-endy)
Zrange=abs(startz-endz)
print("{},{},{}".format(Xrange,Yrange,Zrange))

for i in range(Xrange):
    mc.setBlock(startx+i,starty,startz+i,randomBlock())
    time.sleep(0.5)
for j in range(Zrange):
    mc.setBlock(startx+j,starty,startz+j,randomBlock())
    time.sleep(0.5)