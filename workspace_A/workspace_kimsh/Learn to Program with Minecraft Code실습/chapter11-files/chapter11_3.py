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
    
#===============================================================================
# for i in range(len(player)):
#     print(player[len(player)-len(player)][len(player)+i])
#     
#===============================================================================
    
    
       
    
    
#===============================================================================
# mc.postToChat()
# player2=open("player2","wb")
# pickle.dump(player,player2)
# player2.close()
#===============================================================================

with open("player2","rb") as player2:
    data=pickle.load(player2)
    print(data)
