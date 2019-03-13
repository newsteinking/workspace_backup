from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time
import pickle
count=0

player=[]
player2=""

tofile=""
while count<5:
    x,y,z=mc.player.getPos()
    Postuple=int(x),int(y),int(z),block.WOOD.id
    Poslist=list(Postuple)
    player.append(Poslist)
    time.sleep(1)
    count+=1
  
with open("player3","wb") as f:
    pickle.dump(player,f)
    
with open("player3","rb") as f:
    data=pickle.load(f)
    print(data)