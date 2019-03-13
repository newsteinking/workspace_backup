from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
import random


x,y,z=mc.player.getPos()

def brokenBlock():
    brokenBlocks = [48, 67, 4, 4, 4, 4]
    block = random.choice(brokenBlocks)
    return block

def randomBlock():
    brokenBlocks = [103, 103, 103, 103, 103, 103]
    block = random.choice(brokenBlocks)
    return block


history=[]
time.sleep(2)
count=0
# for i in range(10):
while count <20:
    x1,y1,z1=mc.player.getPos()
    position=int(x1),int(y1),int(z1),brokenBlock()
    print(list(position))
    a=list(position)
    history.append(a)
    time.sleep(2)
    count+=1


print(history)
oldhistory=history

history.sort()
print(history)
print(history[len(history)-len(history)][0])
print(history[len(history)-1][0])
print(history[len(history)-len(history)][2])
print(history[len(history)-1][2])
startx=history[len(history)-len(history)][0]
widthx=(history[len(history)-1][0])-(history[len(history)-len(history)][0])
starty=history[len(history)-len(history)][1]
startz=history[len(history)-len(history)][2]
widthz=(history[len(history)-1][2])-(history[len(history)-len(history)][2])
print(widthx)
print(widthz)
mc.setBlocks(startx,starty,startz,startx+widthx,starty,startz+widthz,randomBlock())

for hist in oldhistory:
    mc.setBlock(hist)









