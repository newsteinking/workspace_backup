from mcpi.minecraft import Minecraft
bibi=Minecraft.create()
import time 

bibi.postToChat("test")

time.sleep(1)

j=bibi.player.getPos()
x=j.x
y=j.y
z=j.z
j2=bibi.getBlock(x,y,z)
bibi.postToChat(j2)

time.sleep(1)

air=0
Air= j2 == air

NotAir=j2!=air

if Air==True:
    bibi.postToChat("I am in air.")
    
else:
    bibi.postToChat("I am in ground.")
    
time.sleep(1)

if NotAir==True:
    bibi.postToChat("I am in ground.")
    
else:
    bibi.postToChat("I am in air.")
    
    

