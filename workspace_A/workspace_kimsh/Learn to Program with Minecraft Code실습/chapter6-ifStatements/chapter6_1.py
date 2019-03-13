from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
front=3

q=input("create your block? : ")
if q=="yes":
    BlockType=int(input("input your block type. : "))
    mc.setBlock(x+front,y,z,BlockType)
    
else:
    mc.postToChat("Ok...")